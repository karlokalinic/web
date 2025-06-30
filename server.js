const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.json());

// Glavni endpoint za callback koji Suno koristi
app.post('/suno-callback', (req, res) => {
  console.log('Primljen callback od Suno!');
  console.log(JSON.stringify(req.body, null, 2)); // ispiši cijeli sadržaj
  res.status(200).send('OK');
});

// Basic root
app.get('/', (req, res) => {
  res.send('Suno Callback Server radi! 🚀');
});

app.listen(PORT, () => {
  console.log(`Server sluša na http://localhost:${PORT}`);
});
