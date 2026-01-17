/**
 * Referral Engine for Project OVERLORD
 * Handles invitation tracking and credit allocation.
 */

export const generateReferralLink = (userId: string): string => {
  const baseUrl = process.env.NEXT_PUBLIC_APP_URL || 'https://overlord.ai';
  return `${baseUrl}/signup?ref=${userId}`;
};

export const processReferral = async (referredUserId: string, referrerCode: string) => {
  try {
    // API call to backend to validate code and link accounts
    const response = await fetch('/api/growth/referral', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        newUserId: referredUserId,
        code: referrerCode,
        event: 'SIGNUP_COMPLETED'
      })
    });
    
    return await response.json();
  } catch (error) {
    console.error("Referral Processing Failed:", error);
    return null;
  }
};

export const REWARD_TIERS = {
  BRONZE: { invites: 1, reward: "1 Premium Export" },
  SILVER: { invites: 5, reward: "5 Premium Exports + No Watermark" },
  GOLD: { invites: 10, reward: "1 Month Pro Plan" }
};