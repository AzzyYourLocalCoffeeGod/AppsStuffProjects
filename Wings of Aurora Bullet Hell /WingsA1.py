<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wings of Aurora - Prologue</title>
  <style>
    body {
      margin: 0;
      background-color: #000000;
      overflow: hidden;
      font-family: 'Courier New', monospace;
      color: #00ff00;
    }
    canvas {
      background: #001100;
      display: block;
      margin: 20px auto;
      border: 3px solid #00ff00;
      image-rendering: pixelated;
    }
    #ui {
      position: absolute;
      top: 10px;
      left: 10px;
      color: #00ff00;
      font-size: 18px;
      display: none; /* Hidden during prologue */
    }
  </style>
</head>
<body>
  <div id="ui">Level: <span id="level">1</span> | Lives: <span id="lives">3</span> | Score: <span id="score">0</span></div>
  <canvas id="c" width="1080" height="720"></canvas>

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
      "The Lattice laughs:",
      "“You will never complete the Covenant.”",
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
        ctx.font = 'bold 28px Courier New';
        ctx.textAlign = 'center';

        // Auto-advance every ~3 seconds
        prologueTimer++;
        if (prologueTimer % 180 === 0 && prologueLine < prologue.length) {
          prologueLine++;
        }

        // Render lines with better spacing for wider canvas
        for (let i = 0; i < prologueLine; i++) {
          const y = 180 + i * 45;  // More vertical breathing room
          ctx.fillText(prologue[i], canvas.width / 2, y);
        }

        // Final prompt - lower and larger
        if (prologueLine >= prologue.length) {
          ctx.fillStyle = '#ffff00';
          ctx.font = '32px Courier New';
          ctx.fillText('Press SPACE to begin the rescue.', canvas.width / 2, canvas.height - 100);
        }

        // Start game on SPACE
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
