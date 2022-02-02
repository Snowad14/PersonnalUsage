const mineflayer = require('mineflayer')
const antiafk = require("mineflayer-antiafk");
const { killaura } = require('mineflayer-antiafk/lib/modules');

const bot = mineflayer.createBot({
    host: '', // minecraft server ip
    username: '', // minecraft username
    password: '', // minecraft password, comment out if you want to log into online-mode=false servers
    // port: 25565,                // only set if you need a port that isn't 25565
    version: "1.18",             // only set if you need a specific version or snapshot (ie: "1.8.9" or "1.16.5"), otherwise it's set automatically
    auth: 'mojang'              // only set if you need microsoft auth, then set this to 'microsoft'
  }) 

  /*
bot.on('chat', (username, message) => {
  if (username === bot.username) return
  console.log(message)
}) */

const { mineflayer: mineflayerViewer } = require('prismarine-viewer')
bot.once('spawn', () => {
  mineflayerViewer(bot, { port: 3007, firstPerson: false }) // port is the minecraft server port, if first person is false, you get a bird's-eye view
})

function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  }


bot.loadPlugin(antiafk);

bot.on('spawn', () => {
    console.log("connected")
    bot.setQuickBarSlot(4)
    bot.activateItem()
    bot.afk.setOptions({ fishing: false, actions: ['jump', 'rotate', 'walk'], killauraEnabled: false}); //disables fishing
    bot.afk.start();
  })

bot.on('windowOpen', (window) => {
    console.log('window open')
    bot.clickWindow(20,0,0)
  })
    
bot.on('windowClose', (window) => {
    console.log('window closed')
  })

bot.on('messagestr', (string) => {
    console.log(string)
    if (string.includes("Le premier joueur qui écrit")) {
        var myWord = "ok"
        if (string.includes("gagnera")) {
            myWord = string.match("écrit (.*) gagnera")[1];
        }
        if (string.includes("remportera")) {
            myWord = string.match("écrit (.*) remportera")[1];
        }

        var finalword = myWord;
        if (finalword[0] == "'" && finalword.slice(-1) == "'") {
            finalword = finalword.substring(1, finalword.length-1);
        }
    
        var multiplicateur = finalword.length * 100;
        var random = getRandomInt(1000 * multiplicateur, 1100 * multiplicateur)
        sleep(random);
        bot.chat(finalword)
    }

    if (string.includes("Le premier joueur qui résout le calcul")) {
        var myWord = "ok"
        if (string.includes("gagnera")) {
            myWord = string.match("calcul (.*) gagnera")[1];
        }
        if (string.includes("remportera")) {
            myWord = string.match("calcul (.*) remportera")[1];
        }
        if (string.includes(" x ")) {
            myWord = myWord.replace(" x ", " * ")
        }
        var finalword = eval(myWord)
        sleep(getRandomInt(1400, 2100));
        bot.chat(finalword)
    }

    if (string.includes("(Snowad14 ➠ Vous) ")) {
      string = string.replace("(Snowad14 ➠ Vous) ", '')
      bot.chat(string)
      /*
      var args = string.split(" ").slice(1)

      
      if (string.startsWith("pay"))
      {
        var moneyToSend = args.join(" ");
        bot.chat("/pay Snowad14 " + moneyToSend)

      } */
  }

  })

// Log errors and kick reasons:
bot.on('kicked', console.log)
bot.on('error', console.log)