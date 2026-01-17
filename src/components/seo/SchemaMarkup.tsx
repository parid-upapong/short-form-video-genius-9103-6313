import React from 'react';

const SchemaMarkup = () => {
  const schema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Overlord AI",
    "operatingSystem": "Web/Cloud",
    "applicationCategory": "MultimediaApplication",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "1240"
    },
    "description": "Revolutionary AI platform that transforms text prompts into viral short-form videos for TikTok and Instagram Reels."
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
};

export default SchemaMarkup;