const express = require('express'); 
const app = express();
app.use(express.json());

app.post('/callback', (req, res) => { 
  console.log('POST primljen:', req.body); 
  res.status(200).send('OK');
}); 

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Backend server na portu ${PORT}`); 
});
