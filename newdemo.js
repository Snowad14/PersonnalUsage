// Require puppeteer extra and puppeteer stealth
const puppeteer = require("puppeteer-extra");
const pluginStealth = require("puppeteer-extra-plugin-stealth");

// Require our hcaptcha method
const { hcaptcha } = require("hcaptcha-puppeteer");

// Tell puppeteer to use puppeteer stealth
puppeteer.use(pluginStealth());

(async () => {
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

    // Send page to your url
    await page.goto("https://serveur-prive.net/minecraft/storycraft-survie-1-18-1-nouveaux-monstres-6911/vote");

    // Remove the page's default timeout function
    await page.setDefaultNavigationTimeout(0);

    const startTime = Date.now();
    
    // Call hcaptcha method passing in our page
    try {
        await hcaptcha(page);
    } catch (error) {
        console.log("error")
    }

    const endTime = Date.now();
    console.log(`Completed in ${(endTime - startTime) / 1000} seconds`);

    // Your page is ready to submit.
    // Captcha solving should be the last function on your page so we
    // don't have to worry about the response token expiring.
    /**
     * Example:
     * await page.click("loginDiv > loginBtn");
     */
})();