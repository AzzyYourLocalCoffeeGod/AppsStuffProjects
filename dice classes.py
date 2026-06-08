

<body>
  <div id="title" class="neon">Azrael's D&D Dice Oracle</div>

  <div class="inputs">
    <label>Die: 
      <select id="dieType">
        <option value="4">d4</option>
        <option value="6">d6</option>
        <option value="8">d8</option>
        <option value="10">d10</option>
        <option value="12">d12</option>
        <option value="20" selected>d20</option>
        <option value="100">d100</option>
      </select>
    </label>

    <label>Quantity: 
      <input type="number" id="quantity" value="1" min="1" max="100">
    </label>

    <label>Modifier: 
      <input type="number" id="modifier" value="0">
    </label>

    <label>
      <input type="checkbox" id="advantage"> Advantage
      <input type="checkbox" id="disadvantage"> Disadvantage
    </label>

    <br><br>
    <button onclick="roll()">ROLL THE BONES</button>
    <button onclick="clearHistory()">CLEAR HISTORY</button>
  </div>

  <div id="result" class="neon">Ready to roll...</div>
  <div id="history"></div>
  <div id="sprite">🎲</div>

  <script>
    let history = [];

    function rollDie(sides) {
      return Math.floor(Math.random() * sides) + 1;
    }

    function roll() {
      const die = parseInt(document.getElementById('dieType').value);
      let qty = parseInt(document.getElementById('quantity').value);
      const mod = parseInt(document.getElementById('modifier').value) || 0;
      const adv = document.getElementById('advantage').checked;
      const dis = document.getElementById('disadvantage').checked;

      let rolls = [];
      for (let i = 0; i < qty; i++) {
        rolls.push(rollDie(die));
      }

      let final = rolls.reduce((a, b) => a + b, 0) + mod;

      // Advantage/Disadvantage
      if (adv || dis) {
        const extra = [];
        for (let i = 0; i < qty; i++) extra.push(rollDie(die));
        const best = rolls.map((r, i) => Math.max(r, extra[i]));
        const worst = rolls.map((r, i) => Math.min(r, extra[i]));
        rolls = adv ? best : worst;
        final = rolls.reduce((a, b) => a + b, 0) + mod;
      }

      // Display
      const resultsDiv = document.getElementById('result');
      resultsDiv.innerHTML = rolls.map((r, i) => 
        `<span class="die">${r}</span>` + (i < rolls.length - 1 ? ' + ' : '')
      ).join('') + (mod !== 0 ? ` + ${mod}` : '') + 
        `<br><span class="neon" style="font-size:42px;">Total: ${final}</span>`;

      const expr = `${qty}d${die}${adv ? ' (Adv)' : dis ? ' (Dis)' : ''}${mod !== 0 ? (mod > 0 ? '+' : '') + mod : ''}`;
      history.unshift(`${expr} → ${final} [${rolls.join(', ')}]`);
      if (history.length > 15) history.pop();
      updateHistory();
    }

    function updateHistory() {
      const histDiv = document.getElementById('history');
      histDiv.innerHTML = history.map(item => `<div class="history-item">${item}</div>`).join('');
    }

    function clearHistory() {
      history = [];
      updateHistory();
    }

    // Typing title
    const title = document.getElementById('title');
    const fullTitle = "Azrael's D&D Dice Oracle";
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
