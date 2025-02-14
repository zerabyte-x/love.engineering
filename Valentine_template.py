##"<a href=\"https://colab.research.google.com/github/zerabyte-x/love.engineering/blob/main/Valentine_template.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
%%html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Romantic Valentine Card</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Pacifico&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #ff99cc, #ffccff, #ff99cc);
            overflow: hidden;
            font-family: 'Dancing Script', cursive;
        }

        .container {
            position: relative;
            width: 75%;
            max-width: 560px;
        }

        .envelope {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 240px;
            height: 160px;
            cursor: pointer;
            transition: all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.1));
            z-index: 1;
        }

        .envelope-front {
            position: absolute;
            width: 100%;
            height: 100%;
            background: linear-gradient(160deg, #ff3860 40%, #ff1493 100%);
            clip-path: polygon(0 0, 100% 0, 100% 85%, 50% 100%, 0 85%);
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            font-size: 1.8em;
            text-align: center;
            font-family: 'Pacifico', cursive;
        }

        .envelope-back {
            position: absolute;
            width: 85%;
            height: 85%%;
            background: linear-gradient(45deg, #ff85a2, #ff6090);
            transform: translateY(-15px);
            border-radius: 4px;
        }

        .letter {
            position: relative;
            width: 100%;
            height: 0;
            background: linear-gradient(135deg, #fff5f5 0%, #ffe6e6 100%);
            padding: 0;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            z-index: 2;
            opacity: 0;
            transition: all 1s ease;
        }

        .letter.open {
            height: auto;
            padding: 30px;
            opacity: 1;
        }

        .message {
            font-family: 'Dancing Script', cursive;
            font-size: 1.4em;
            color: black;
            opacity: 1;
            transform: translateY(20px);
            transition: all 0.8s ease;
        }

        .message.show {
            opacity: 1;
            transform: translateY(0);
        }

        .smoke-particle {
            position: absolute;
            width: 8px;
            height: 8px;
            background: rgba(255,255,255,0.9);
            border-radius: 50%;
            pointer-events: none;
            animation: smoke-drift 4s ease-out forwards;
        }

        @keyframes smoke-drift {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-100px) scale(3); opacity: 0; }
        }

        .floating-item {
            position: fixed;
            pointer-events: none;
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(-5deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="envelope" onclick="toggleEnvelope()">
            <div class="envelope-back"></div>
            <div class="envelope-front">
                To,<br>My love ❤️
            </div>
        </div>
        <div class="letter">
            <div class="message">
                <h1> Hey ❤️, </h1>
                <p>.......✨.</p>
                <p>....... but I promise I'm paying attention.</p>
                <p>But I'm pretty good at one thing - knowing that you're my favorite part of every single day 💫.</p>
                <p>I'm out of words...🤍.</p>
                <p>Yours,</p>
                <p>Utkarsh</p>
                <p>P.S. Happy Valentine's Day, my favorite person 💝</p>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
    <script>
        let isOpen = false;
        let smokeParticles = [];
        let floatingInterval;

        function toggleEnvelope() {
            if (!isOpen) {
                createSmoke();
                createFloatingItems();

                anime({
                    targets: '.envelope',
                    top: '-120px',
                    left: '-120px',
                    rotate: '-20deg',
                    easing: 'easeInOutQuad',
                    duration: 1000
                });

                anime({
                    targets: '.letter',
                    height: 'auto',
                    padding: '30px',
                    opacity: 1,
                    easing: 'easeInOutQuad',
                    duration: 1000
                });

                anime({
                    targets: '.message > *',
                    opacity: [0, 1],
                    translateY: [20, 0],
                    delay: anime.stagger(100),
                    easing: 'easeOutElastic(1, .8)'
                });

                document.querySelector('.letter').classList.add('open');
                document.querySelectorAll('.message > *').forEach(element => element.classList.add('show'));

                isOpen = true;
            } else {
                anime({
                    targets: '.message > *',
                    opacity: [1, 0],
                    translateY: [0, 20],
                    delay: anime.stagger(100),
                    easing: 'easeInElastic(1, .8)'
                });

                anime({
                    targets: '.envelope',
                    top: '50%',
                    left: '50%',
                    rotate: '0deg',
                    easing: 'easeInOutQuad',
                    duration: 1000
                });

                anime({
                    targets: '.letter',
                    height: '0',
                    padding: '0',
                    opacity: 0,
                    easing: 'easeInOutQuad',
                    duration: 1000
                });

                document.querySelector('.letter').classList.remove('open');
                document.querySelectorAll('.message > *').forEach(element => element.classList.remove('show'));

                removeSmoke();
                stopFloatingItems();
                isOpen = false;
            }
        }

        function createSmoke() {
            for(let i = 0; i < 15; i++) {
                const smoke = document.createElement('div');
                smoke.className = 'smoke-particle';
                smoke.style.left = `${50 + Math.random() * 20 - 10}%`;
                smoke.style.top = '50%';
                smoke.style.animationDelay = `${i * 0.1}s`;
                document.body.appendChild(smoke);
                smokeParticles.push(smoke);
            }
        }

        function removeSmoke() {
            smokeParticles.forEach(smoke => smoke.remove());
            smokeParticles = [];
        }

        function createFloatingItems() {
            const items = ['❤️', '💕', '✨', '💗', '💓', '💞', '😘', '😍', '😘'];
            floatingInterval = setInterval(() => {
                const item = items[Math.floor(Math.random() * items.length)];
                createFloatingItem(item);
            }, 400);
        }

        function createFloatingItem(content) {
            const item = document.createElement('div');
            item.className = 'floating-item animate__animated animate__heartBeat';
            item.style.left = Math.random() * 100 + 'vw';
            item.style.top = Math.random() * 100 + 'vh';
            item.style.fontSize = (Math.random() * 20 + 20) + 'px';
            item.innerHTML = content;

            if(!['❤️', '💕', '✨'].includes(content)) {
                item.style.fontFamily = 'Pacifico, cursive';
                item.style.color = '#ff1493';
            }

            document.body.appendChild(item);
            setTimeout(() => item.remove(), 5000);
        }

        function stopFloatingItems() {
            clearInterval(floatingInterval);
            document.querySelectorAll('.floating-item').forEach(item => item.remove());
        }
    </script>
</body>
</html>
