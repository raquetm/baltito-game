document.addEventListener("DOMContentLoaded", () => {
    const dog = document.getElementById("dog");
    const dogImg = dog.querySelector("img");
    const flower = document.getElementById("flower");
    const scoreElement = document.getElementById("score");
    const background = document.getElementById("background");

    let isJumping = false;
    let isWalking = true;
    let walkFrame = 1;
    let score = 0;
    let gameOver = false;
    let backgroundPosition = 0;
    let speed = 2; 

    // alternar entre las imágenes de balto caminando
    function walkAnimation() {
        if (isWalking) {
            walkFrame = walkFrame === 1 ? 2 : 1;
            dogImg.src = `/static/img/game/baltoWalking${walkFrame}.png`; 
        }
    }

    setInterval(walkAnimation, 300); // cambia de imagen cada 0.3s

   function jump() {
    if (!isJumping && !gameOver) {
        isJumping = true;
        isWalking = false;
        dogImg.src = `/static/img/game/baltoJumps.png`;

        dog.classList.add("jump");

        // asegurar que la animación termine antes de resetear
        setTimeout(() => {
            dog.classList.remove("jump");
            isJumping = false;
            isWalking = true;
        }, 700);
    }
}

document.addEventListener("keydown", (event) => {
    if ((event.code === "Space" || event.key === "ArrowUp") && !gameOver) {
        jump();
    }
});

function checkCollision() {
    const dogRect = dog.getBoundingClientRect();
    const flowerRect = flower.getBoundingClientRect();

    //zona de colisión reducida
    const collisionMarginX = 70; 
    const collisionMarginY = 40; 

    if (
        dogRect.left + collisionMarginX < flowerRect.right - collisionMarginX &&
        dogRect.right - collisionMarginX > flowerRect.left + collisionMarginX &&
        dogRect.top + collisionMarginY < flowerRect.bottom - collisionMarginY &&
        dogRect.bottom - collisionMarginY > flowerRect.top + collisionMarginY
    ) {
        gameOver = true;
        showGameOverModal(); // mostrar la ventana de Game Over
    }
}

function showGameOverModal() {
    const playerName = prompt("Input your name:") || "Anonymous player"; // pedir nombre del jugador
    const modal = document.getElementById("gameOverModal");
    const scoreText = document.getElementById("playerScore");

    scoreText.textContent = `${playerName}, your score is: ${score}`;
    modal.style.display = "flex"; 

    // reiniciar el juego
    document.getElementById("restartButton").addEventListener("click", () => {
        location.reload(); 
    });

    // ir a la página de reseñas 
    document.getElementById("reviewButton").addEventListener("click", () => {
        window.location.href = "";
    });

    // ir a la página de inicio
    document.getElementById("homeButton").addEventListener("click", () => {
        window.location.href = ""; 
    });
}

function updateScore() {
        if (!gameOver) {
            score++;
            scoreElement.textContent = `Score: ${score}`;
        }
    }

    setInterval(updateScore, 100); // incrementa la puntuación cada 0.1s

function gameLoop() {
        if (!gameOver) {
            checkCollision();
            requestAnimationFrame(gameLoop);
        }
}
function moveBackground() {
        if (!gameOver) {
            backgroundPosition -= speed; 
            background.style.backgroundPosition = `${backgroundPosition}px 0`; 
            requestAnimationFrame(moveBackground); 
        }
    }

    moveBackground(); 

    gameLoop(); // inicia el bucle del juego
});

