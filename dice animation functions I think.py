function rollDice(sides) {
  const num = parseInt(document.getElementById('numDice').value);
  const mod = parseInt(document.getElementById('modifier').value) || 0;
  const adv = document.getElementById('advantage').checked;
  const dis = document.getElementById('disadvantage').checked;

  let rolls = [];
  for (let i = 0; i < num; i++) {
    rolls.push(rollDie(sides));
  }

  let final = rolls.reduce((a, b) => a + b, 0) + mod;

  if (adv && !dis) {
    const advRoll = rollDie(sides);
    rolls.push(advRoll);
    final = Math.max(...rolls) + mod;
  }
  if (dis && !adv) {
    const disRoll = rollDie(sides);
    rolls.push(disRoll);
    final = Math.min(...rolls) + mod;
  }

  const resultsDiv = document.getElementById('result');
  resultsDiv.innerHTML = rolls.map(roll => `<span class="die">${roll}</span>`).join('') + 
    `<br><span class="neon" style="font-size: 36px;">Total: ${final}</span>`;
  
  let note = '';
  if (adv) note += ' (Advantage)';
  if (dis) note += ' (Disadvantage)';
  
  history.unshift(`${num}d${sides}${note} ${mod >= 0 ? '+' : ''}${mod} = ${final} (${rolls.join(', ')})`);
  if (history.length > 20) history.pop();
  updateHistory();
}
