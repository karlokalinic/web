const express = require('express');
const app = express();

app.use(express.json());

// Dodaj rutu za GET / da odgovara nečim
app.get('/', (req, res) => {
  res.send('Backend server radi. POST na /callback je spreman.');
});

app.post('/callback', (req, res) => {
  console.log('POST primljen:', req.body);
  res.status(200).send('OK');
});

const PORT = process.env.PORT || 3000;
// Pokreni server na definiranom portu
app.listen(PORT, () => {
  console.log(`Backend server na portu ${PORT}`);
});
