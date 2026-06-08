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
    .inputs {
      margin: 2rem 0;
    }
    input {
      background: #001100;
      border: 2px solid #0ff;
      color: #0ff;
      font-family: 'VT323', monospace;
      font-size: 20px;
      padding: 0.5rem;
      width: 200px;
      text-align: center;
    }
    button {
      background: #0ff;
      border: none;
      color: #000;
      font-family: 'VT323', monospace;
      font-size: 20px;
      padding: 1rem 1.5rem;
      margin: 0.5rem;
      cursor: pointer;
      text-shadow: none;
      box-shadow: 0 0 10px #0ff;
      transition: all 0.3s;
    }
    button:hover {
      box-shadow: 0 0 20px #0ff, 0 0 30px #0ff;
      transform: scale(1.05);
    }
    #result {
      font-size: 48px;
      margin: 2rem 0;
      line-height: 1.2;
      animation: glow 1s ease-in-out infinite alternate;
    }
    @keyframes glow {
      from { text-shadow: 0 0 10px #0ff; }
      to { text-shadow: 0 0 20px #0ff; 0 0 30px #0ff; }
    }
    .die {
      display: inline-block;
      margin: 0.5rem;
      padding: 1rem;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #0ff;
      animation: rollIn 0.6s ease-out;
      min-width: 50px;
    }
    @keyframes rollIn {
      from { transform: scale(0.5) rotate(360deg); opacity: 0; }
      to { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    #history {
      max-height: 250px;
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
      animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    #sprite {
      position: fixed;
      bottom: 20px;
      right: 20px;
      font-size: 48px;
      animation: bounce 2s ease-in-out infinite;
    }
    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }
  </style>
</head>
<body>
  <div id="title" class="neon">Azrael's D&D Dice Roller</div>
  
  <div class="inputs">
    <input type="text" id="expression" placeholder="e.g. 4d6+2 or 2d20kh1" value="1d20">
    <br>
    <button onclick="roll()">ROLL</button>
    <button onclick="clearHistory()">CLEAR HISTORY</button>
  </div>
  
  <div id="result" class="neon">Enter expression & roll!</div>
  
  <div id="history"></div>
  
  <div id="sprite">🎲</div>

  <script>
    let history = [];

    function rollDie(sides) {
      return Math.floor(Math.random() * sides) + 1;
    }

    function parseExpression(expr) {
      // Parse NdX+Y, support kh1 (keep highest 1 = advantage)
      const match = expr.match(/(\d*)d(\d+)([khl]?\d?)([\+\-]?\d+)?/i);
      if (!match) return null;

      const numDice = match[1] ? parseInt(match[1]) : 1;
      const sides = parseInt(match[2]);
      const keep = match[3]; // 'kh1' = keep highest 1
      const mod = match[4] ? parseInt(match[4]) : 0;

      const rolls = [];
      for (let i = 0; i < numDice; i++) {
        rolls.push(rollDie(sides));
      }

      let final = rolls.reduce((a, b) => a + b, 0);
      if (keep === 'kh1') {
        final = Math.max(...rolls);
      } else if (keep === 'kl1') {
        final = Math.min(...rolls);
      }
      final += mod;

      return { rolls, final, expr };
    }

    function roll() {
      const expr = document.getElementById('expression').value.trim();
      const result = parseExpression(expr);

      if (!result) {
        document.getElementById('result').textContent = 'Invalid expression!';
        return;
      }

      const resultsDiv = document.getElementById('result');
      resultsDiv.innerHTML = result.rolls.map(roll => `<span class="die">${roll}</span>`).join('') + 
        `<br><span class="neon" style="font-size: 36px;">Total: ${result.final}</span>`;
      
      history.unshift(`${expr} = ${result.final} (${result.rolls.join(', ')})`);
      if (history.length > 20) history.pop();
      updateHistory();
    }

    function updateHistory() {
      const histDiv = document.getElementById('history');
      histDiv.innerHTML = history.map((item, i) => `<div class="history-item">${item}</div>`).join('');
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

    // Preset buttons
    document.addEventListener('DOMContentLoaded', () => {
      const presets = [
        '1d20', '2d20kh1','2d20kl1', '4d6kh3', '1d20+5', '2d6+3'
      ];
      presets.forEach(preset => {
        const btn = document.createElement('button');
        btn.textContent = preset;
        btn.onclick = () => document.getElementById('expression').value = preset;
        document.querySelector('.inputs').appendChild(btn);
      });
    });
  </script>
</body>
</html>
