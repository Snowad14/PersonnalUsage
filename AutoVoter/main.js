// Require puppeteer extra and puppeteer stealth
const puppeteer = require("puppeteer-extra");
const pluginStealth = require("puppeteer-extra-plugin-stealth");
const fs = require('fs').promises;

// Require our hcaptcha method
const { hcaptcha } = require("hcaptcha-puppeteer");

// Tell puppeteer to use puppeteer stealth
puppeteer.use(pluginStealth());

(async () => {

    const startTime = Date.now();
    console.log('started')
    // Instantiate a new browser object
    // Ignore errors associated to https
    // Can be headless but for example sake we want to show the browser
    // Set your desired arguments for your puppeteer browser
    const browser = await puppeteer.launch({
        ignoreHTTPSErrors: true,
        headless: false,
        args: [
            `--window-size=600,1000`,
            "--window-position=000,000",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            '--user-data-dir="/tmp/chromium"',
            "--disable-web-security",
            "--disable-features=site-per-process",
        ],
    });

    // Get browser pages
    const [page] = await browser.pages();

    
    const cookiesString = await fs.readFile('./cookies.json');
    const cookies = JSON.parse(cookiesString);
    await page.setCookie(...cookies);
    await page.goto("https://storycraft.fr/vote");
    
    const elements = await page.$x('//*[@id="app"]/main/div[2]/div[2]/div[2]/div[2]/a[1]');
    
    const [newPage] = await Promise.all([
        new Promise(resolve => page.once('popup', resolve)),
        await elements[0].click(),
    ]);

    await hcaptcha(newPage);
    await newPage.waitForSelector(".fc-footer-buttons > button")
    await newPage.click(".fc-footer-buttons > button");
    await newPage.type('#pseudo', 'Snowad14', {delay: 20})
    
    //await hcaptcha(newPage);


    const endTime = Date.now();
    console.log(`Completed in ${(endTime - startTime) / 1000} seconds`);

    //await browser.close(); 

    // Your page is ready to submit.
    // Captcha solving should be the last function on your page so we
    // don't have to worry about the response token expiring.
    /**
     * Example:
     * await page.click("loginDiv > loginBtn");
     */
})();