document.addEventListener("DOMContentLoaded", () => {
    const dog = document.getElementById("dog");
    const dogImg = dog.querySelector("img");
    const flower = document.getElementById("flower");
    const scoreElement = document.getElementById("score");
    const background = document.getElementById("background");
    const saveScoreForm = document.getElementById("saveScoreForm");
    const scoreInput = document.getElementById("scoreInput");

    const instructionsModal = document.getElementById("instructionsModal");
    const playButton = document.getElementById("playButton");

    let isJumping = false;
    let isWalking = false;
    let walkFrame = 1;
    let score = 0;
    let gameOver = false;
    let backgroundPosition = 0;
    let speed = 2;
    let gameStarted = false;
    let animationFrameId;
    let scoreInterval;
    let walkInterval;

    function startWalkingAnimation() {
        if (!walkInterval) {
            walkInterval = setInterval(() => {
                if (!isJumping && !gameOver && gameStarted) {
                    walkFrame = walkFrame === 1 ? 2 : 1;
                    dogImg.src = `/static/img/game/baltoWalking${walkFrame}.png`;
                }
            }, 300); 
        }
    }

    function stopWalkingAnimation() {
        clearInterval(walkInterval);
        walkInterval = null;
    }

    function jump() {
        if (!isJumping && !gameOver && gameStarted) {
            isJumping = true;
            isWalking = false;
            stopWalkingAnimation(); 

            dogImg.src = `/static/img/game/baltoJumps.png`;
            dog.classList.add("jump");

            setTimeout(() => {
                dog.classList.remove("jump");
                isJumping = false;
                isWalking = true;
                startWalkingAnimation(); 
            }, 700);
        }
    }

    document.addEventListener("keydown", (event) => {
        if ((event.code === "Space" || event.key === "ArrowUp") && !gameOver && gameStarted) {
            jump();
        }
    });

    function checkCollision() {
        if (!gameStarted || gameOver) return;

        const dogRect = dog.getBoundingClientRect();
        const flowerRect = flower.getBoundingClientRect();

        const collisionMarginX = 70;
        const collisionMarginY = 40;

        if (
            dogRect.left + collisionMarginX < flowerRect.right - collisionMarginX &&
            dogRect.right - collisionMarginX > flowerRect.left + collisionMarginX &&
            dogRect.top + collisionMarginY < flowerRect.bottom - collisionMarginY &&
            dogRect.bottom - collisionMarginY > flowerRect.top + collisionMarginY
        ) {
            gameOver = true;
            showGameOverModal();
        }
    }

    function showGameOverModal() {
        const modal = document.getElementById("gameOverModal");
        const scoreText = document.getElementById("playerScore");

        scoreText.textContent = `Your score is: ${score}`;
        scoreInput.value = score;

        console.log("📤 Score set in input:", scoreInput.value);

        modal.style.display = "flex";

        stopGame();

        document.getElementById("restartButton").addEventListener("click", () => {
            location.reload();
        });

        document.getElementById("homeButton").addEventListener("click", () => {
            window.location.href = "/";
        });
    }

    function stopGame() {
        gameStarted = false;
        flower.classList.remove("playing");
        cancelAnimationFrame(animationFrameId);
        clearInterval(scoreInterval);
        stopWalkingAnimation(); 
    }

    saveScoreForm.addEventListener("submit", function (event) {
        scoreInput.value = score;

        if (!scoreInput.value || isNaN(scoreInput.value) || scoreInput.value <= 0) {
            event.preventDefault();
            console.error("❌ No score provided!");
            alert("Error: Score is missing!");
        } else {
            console.log("✅ Score sent successfully:", scoreInput.value);
            window.location.href = "/leaderboard/";
        }
    });

    function updateScore() {
        if (!gameOver && gameStarted) {
            score++;
            scoreElement.textContent = `Score: ${score}`;
        }
    }

    function gameLoop() {
        if (!gameOver && gameStarted) {
            checkCollision();
            animationFrameId = requestAnimationFrame(gameLoop);
        }
    }

    function moveBackground() {
        if (!gameOver && gameStarted) {
            backgroundPosition -= speed;
            background.style.backgroundPosition = `${backgroundPosition}px 0`;
            animationFrameId = requestAnimationFrame(moveBackground);
        }
    }

    instructionsModal.style.display = "flex";

    playButton.addEventListener("click", () => {
        instructionsModal.style.display = "none";
        gameStarted = true;
        isWalking = true;

        flower.classList.add("playing");

        moveBackground();
        gameLoop();
        startWalkingAnimation(); 
        scoreInterval = setInterval(updateScore, 100);
    });
});
