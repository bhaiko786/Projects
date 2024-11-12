// This code uses:
// axios to make an HTTP GET request to the InShorts website
// cheerio to parse the HTML response and extract the news headlines
// Here's how the code works:
// Send an HTTP GET request to https://inshorts.com/en/read
// Parse the HTML response using cheerio
// Select all elements with the class news-card
// Iterate through each element and extract:
// Headline: span.news-card-title
// Summary: div.news-card-content
// Link: a attribute href
// Push each extracted news headline to an array newsHeadlines
// Log the newsHeadlines array to the console
// Note: This code only extracts the headlines, summaries, and links from the first page. If you want to scrape multiple pages, you'll need to modify the code to handle pagination.
// Also, keep in mind that web scraping may be subject to the terms of service of the website being scraped. Always respect the website's robots.txt file and terms of service.

const axios = require('axios');
const cheerio = require('cheerio');

axios.get('https://inshorts.com/en/read')
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const newsHeadlines = [];

    $('div.news-card').each(function() {
      const headline = $(this).find('span.news-card-title').text().trim();
      const summary = $(this).find('div.news-card-content').text().trim();
      const link = $(this).find('a').attr('href');

      newsHeadlines.push({ headline, summary, link });
    });

    console.log(newsHeadlines);
  })
  .catch(error => {
    console.error(error);
  });