const { hcaptchaToken } = require("hcaptcha-puppeteer");

(async () => {

    async function test() {
        const startTime = Date.now();
        let token = await hcaptchaToken("https://serveur-prive.net/minecraft/storycraft-survie-1-18-1-nouveaux-monstres-6911/vote");
        const endTime = Date.now();
        console.log(`Completed in ${(endTime - startTime) / 1000} seconds`);
        if (token == null){
            console.log("error retrying")
            test()
        }
        else {
            console.log(token)
        }
      }
    
    test()

      
})();