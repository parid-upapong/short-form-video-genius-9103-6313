# Sitemap: OVERLORD Platform Structure

## 1. Public Facing
- `/` (Landing Page: Value proposition, Demo video, Pricing)
- `/showcase` (Community gallery of AI-generated videos)

## 2. Authentication
- `/login` (Google/Magic Link)
- `/onboarding` (Niche selection, Tone of voice setup)

## 3. Core App (The Studio)
- `/dashboard` (Project history, "New Video" CTA)
- `/create` (The Entry Point: Prompt/Link input)
- `/editor/:id` (The "Frictionless" Editor)
    - `Tab: Script` (Text editor)
    - `Tab: Visuals` (Media library/Replacement)
    - `Tab: Audio` (Voice & BGM settings)
    - `Tab: Style` (Captions & Branding)

## 4. User Workspace
- `/library` (Saved assets, uploaded logos, brand kits)
- `/settings`
    - `Profile`
    - `Billing/Subscription`
    - `API Integrations` (TikTok/Instagram/YouTube API keys)

## 5. Admin (Internal)
- `/admin/queue` (Monitoring render server loads)
- `/admin/users` (Management)