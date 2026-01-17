import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_video_content(user_prompt: str):
    """
    Generates a viral script and image prompts for each scene.
    """
    system_prompt = """
    You are a viral content strategist. Create a 30-second video script.
    Output JSON format:
    {
      "scenes": [
        {"text": "Hook sentence", "image_prompt": "visual description", "duration": 5},
        ...
      ],
      "music_vibe": "energetic"
    }
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Topic: {user_prompt}"}
        ],
        response_format={ "type": "json_object" }
    )
    
    return response.choices[0].message.content