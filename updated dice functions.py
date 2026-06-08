<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Azrael's D&D Dice Roller - Covenant Chaos Edition</title>
  <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
  <style>
    body {
      background: #0a0a0a;
      color: #fff;
      font-family: 'VT323', monospace;
      margin: 0;
      padding: 2rem;
      text-align: center;
      overflow: hidden;
    }
    .neon {
      color: #0ff;
      text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;
      font-size: 24px;
    }
    #title {
      font-size: 32px;
      margin-bottom: 2rem;
    }
    .dice-buttons button {
      background: #0ff;
      border: none;
      color: #000;
      font-size: 20px;
      padding: 0.8rem 1.2rem;
      margin: 0.5rem;
      cursor: pointer;
      box-shadow: 0 0 10px #0ff;
      transition: all 0.3s;
    }
    .dice-buttons button:hover {
      box-shadow: 0 0 20px #0ff;
      transform: scale(1.1);
    }
    .options {
      margin: 1rem 0;
      font-size: 20px;
    }
    select, input {
      background: #001100;
      border: 2px solid #0ff;
      color: #0ff;
      font-family: 'VT323', monospace;
      font-size: 20px;
      padding: 0.5rem;
      margin: 0 0.5rem;
    }
    #result {
      font-size: 48px;
      margin: 2rem 0;
      line-height: 1.2;
      animation: glow 1s ease-in-out infinite alternate;
    }
    @keyframes glow {
      from { text-shadow: 0 0 10px #0ff; }
      to { text-shadow: 0 0 20px #0ff, 0 0 30px #0ff; }
    }
    .die {
      display: inline-block;
      margin: 0.5rem;
      padding: 1rem;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #0ff;
      min-width: 50px;
      animation: rollIn 0.6s ease-out;
    }
    @keyframes rollIn {
      from { transform: scale(0.5) rotate(360deg); opacity: 0; }
      to { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    #history {
      max-height: 200px;
      overflow-y: auto;
      text-align: left;
      margin-top: 2rem;
      padding: 1rem;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #0ff;
    }
    .history-item {
      font-size: 18px;
      margin: 0.5rem 0;
    }
  </style>
</head>
<body>
  <div id="title" class="neon">Azrael's D&D Dice Roller</div>
  
  <div class="dice-buttons">
    <button onclick="rollDice(4)">d4</button>
    <button onclick="rollDice(6)">d6</button>
    <button onclick="rollDice(8)">d8</button>
    <button onclick="rollDice(10)">d10</button>
    <button onclick="rollDice(12)">d12</button>
    <button onclick="rollDice(20)">d20</button>
    <button onclick="rollDice(100)">d100</button>
  </div>
  
  <div class="options">
    Number of dice: 
    <select id="numDice">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3" selected>3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
      <option value="7">7</option>
      <option value="8">8</option>
      <option value="9">9</option>
      <option value="10">10</option>
    </select>
    Modifier: 
    <input type="number" id="modifier" value="0" style="width:60px;">
    <label><input type="checkbox" id="advantage"> Advantage</label>
    <label><input type="checkbox" id="disadvantage"> Disadvantage</label>
  </div>
  
  <button onclick="roll()">ROLL</button>
  <button onclick="clearHistory()">CLEAR HISTORY</button>
  
  <div id="result" class="neon">Enter expression & roll!</div>
  
  <div id="history"></div>

  <script>
    let history = [];

    function rollDie(sides) {
      return Math.floor(Math.random() * sides) + 1;
    }

    function rollDice(sides) {
      const num = parseInt(document.getElementById('numDice').value);
      const mod = parseInt(document.getElementById('modifier').value);
      const adv = document.getElementById('advantage').checked;
      const dis = document.getElementById('disadvantage').checked;

      let rolls = [];
      for (let i = 0; i < num; i++) {
        rolls.push(rollDie(sides));
      }

      let final = rolls.reduce((a, b) => a + b, 0) + mod;

      if (adv) {
        const advRoll = rollDie(sides);
        rolls.push(advRoll);
        final = Math.max(...rolls) + mod;
      }
      if (dis) {
        const disRoll = rollDie(sides);
        rolls.push(disRoll);
        final = Math.min(...rolls) + mod;
      }

      const resultsDiv = document.getElementById('result');
      resultsDiv.innerHTML = rolls.map(roll => `<span class="die">${roll}</span>`).join('') + 
        `<br><span class="neon" style="font-size: 36px;">Total: ${final}</span>`;
      
      history.unshift(`${num}d${sides} ${adv ? 'ADV' : ''} ${dis ? 'DIS' : ''} ${mod >= 0 ? '+' : ''}${mod} = ${final} (${rolls.join(', ')})`);
      if (history.length > 20) history.pop();
      updateHistory();
    }

    function updateHistory() {
      const histDiv = document.getElementById('history');
      histDiv.innerHTML = history.map((item, i) => 
        `<div class="history-item neon">${item}</div>`
      ).join('');
    }

    function clearHistory() {
      history = [];
      updateHistory();
    }

    // Typing title
    const title = document.getElementById('title');
    const fullTitle = 'Azrael\'s D&D Dice Roller';
    title.textContent = '';
    let i = 0;
    function typeTitle() {
      if (i < fullTitle.length) {
        title.textContent += fullTitle.charAt(i);
        i++;
        setTimeout(typeTitle, 150);
      }
    }
    typeTitle();
  </script>
</body>
</html>
