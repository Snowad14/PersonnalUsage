const puppeteer = require("puppeteer-extra");

const url = "https://serveur-prive.net/minecraft/storycraft-survie-1-18-1-nouveaux-monstres-6911/vote";

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: "networkidle2" });

  // cookie
  await page.click(".fc-footer-buttons > button");


})();