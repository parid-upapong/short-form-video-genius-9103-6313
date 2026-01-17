from locust import HttpUser, task, between
import time

class VideoGenerationLoadTester(HttpUser):
    """
    Simulates high-concurrency usage of the OVERLORD API.
    Measures the 'Time-to-Ready' for the 120-second MVP target.
    """
    wait_time = between(1, 5)

    @task
    def generate_and_poll_video(self):
        # 1. Trigger Video Generation
        payload = {
            "prompt": "How to start a side hustle in 2024 using AI",
            "style": "Alex Hormozi"
        }
        
        with self.client.post("/api/v1/generate", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                video_id = response.json().get("job_id")
                self._poll_until_ready(video_id)
            else:
                response.failure(f"Failed to trigger generation: {response.text}")

    def _poll_until_ready(self, video_id):
        start_time = time.time()
        max_wait = 150  # 120s Target + 30s Grace Period
        
        while time.time() - start_time < max_wait:
            with self.client.get(f"/api/v1/status/{video_id}", name="/status/[id]", catch_response=True) as response:
                if response.status_code == 200:
                    status = response.json().get("status")
                    if status == "COMPLETED":
                        total_time = time.time() - start_time
                        # Custom metric for Locust to track E2E Render Speed
                        self.environment.events.request.fire(
                            request_type="RENDER",
                            name="E2E_Generation_Time",
                            response_time=total_time * 1000,
                            response_length=0,
                        )
                        return
                    elif status == "FAILED":
                        response.failure("Video generation task failed internally")
                        return
                
            time.sleep(10)  # Polling interval
            
        self.environment.events.request.fire(
            request_type="RENDER",
            name="E2E_Generation_Time",
            response_time=(time.time() - start_time) * 1000,
            response_length=0,
            exception=TimeoutError("Generation exceeded 150 seconds")
        )