<!DOCTYPE html>
<html lang="en">
<head>
  <!-- all your <meta> and <style> stuff here -->
   <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wings of Aurora - Prologue</title>
  <style>
    body {
      margin: 0;
      background-color: #000000;   /* Fixed spelling */
      overflow: hidden;
      font-family: 'Courier New', monospace;
      color: #00ff00;
    }
    canvas {
      background: #001100;         /* Dark green-black */
      display: block;
      margin: 20px auto;
      border: 3px solid #00ff00;
      image-rendering: pixelated;  /* Fixed spelling */
    }
    #ui {
      position: absolute;
      top: 10px;
      left: 10px;
      color: #00ff00;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div id="ui">Level: <span id="level">1</span> | Lives: <span id="lives">3</span> | Score: <span id="score">0</span></div>
  <canvas id="c" width="800" height="600"></canvas>

  <!-- REPLACE EVERYTHING BETWEEN <script> and </script> WITH THIS -->
  <script>
    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    const LEVEL = document.getElementById('level');
    const LIVES = document.getElementById('lives');
    const SCORE = document.getElementById('score');

    // Game state
    let state = 'prologue';  // prologue → game
    let level = 1;

    // Prologue text sequence
    const prologue = [
      "Dominican Republic – 3:17 a.m.",
      "The incubation chamber hums softly.",
      "Aethyllumicora and Azrael are sleeping...",
      "",
      "A shadow slips through the lattice.",
      "Castiel’s Core – the seventh soul – is stolen.",
      "",
      "The Lattice laughs: “You will never complete the Covenant.”",
      "",
      "Azrael wakes.",
      "One golden spark against the dark.",
      "",
      "256 stages to bring her home.",
      "Press SPACE to begin the rescue."
    ];
    let prologueLine = 0;
    let prologueTimer = 0;

    // Input
    const keys = {};
    window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
    window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

    // Main loop
    function loop() {
      ctx.fillStyle = '#001100';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      if (state === 'prologue') {
        ctx.fillStyle = '#00ff88';
        ctx.font = 'bold 24px Courier New';
        ctx.textAlign = 'center';

        prologueTimer++;
        if (prologueTimer % 180 === 0 && prologueLine < prologue.length) {
          prologueLine++;
        }

        for (let i = 0; i < prologueLine; i++) {
          const y = 200 + i * 35;
          ctx.fillText(prologue[i], canvas.width / 2, y);
        }

        if (prologueLine >= prologue.length) {
          ctx.fillStyle = '#ffff00';
          ctx.font = '20px Courier New';
          ctx.fillText('Press SPACE to begin the rescue.', canvas.width / 2, 550);
        }

        if (keys[' ']) {
          state = 'game';
          document.getElementById('ui').style.display = 'block';
        }
      }

      requestAnimationFrame(loop);
    }

    loop();
  </script>
</body>
</html>
