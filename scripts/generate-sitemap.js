const fs = require('fs');
const globby = require('globby');

async function generateSitemap() {
  const pages = await globby([
    'src/app/**/page.tsx',
    '!src/app/api',
    '!src/app/dashboard',
  ]);

  const sitemap = `
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        ${pages
          .map((page) => {
            const path = page
              .replace('src/app', '')
              .replace('/page.tsx', '')
              .replace('.tsx', '');
            const route = path === '/index' ? '' : path;
            return `
              <url>
                  <loc>${`https://overlord.ai${route}`}</loc>
                  <changefreq>daily</changefreq>
                  <priority>0.7</priority>
              </url>
            `;
          })
          .join('')}
    </urlset>
  `;

  fs.writeFileSync('public/sitemap.xml', sitemap);
  console.log('Sitemap generated successfully.');
}

generateSitemap();