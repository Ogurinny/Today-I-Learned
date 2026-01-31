// Jelas variabel dulu lah aojwoaowaokkoaw
const { Client, LocalAuth, AuthStrategy } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal')

// init clientnyaaaaa :3
const client = new Client({
  authStrategy: new LocalAuth({
    clientId: "Klien-satu"
  }) //biar kagak bolak balikkk
})

client.on('qr', (qr) => {
  qrcode.generate(qr, { small: true });
  console.log("Scan dulu uy")
})

//notif nyaa 
client.on('ready', () => {
  console.log('readyyyyy')
})

client.on('message', message => {
  const pesan = message.body.toLowerCase(); // biar kagak sensitip ama kapital

  if (pesan === 'p') {
    message.reply('Pe');
  }
  if (pesan === 'nig') {
    message.reply('ga')
  };
});

client.initialize();


