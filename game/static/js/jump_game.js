document.addEventListener("DOMContentLoaded", () => {
    const dog = document.getElementById("dog");
    const dogImg = dog.querySelector("img");

    let isJumping = false;
    let isWalking = true;
    let walkFrame = 1;

    // Alternar entre las imágenes de caminar
    function walkAnimation() {
        if (isWalking) {
            walkFrame = walkFrame === 1 ? 2 : 1;
            dogImg.src = `/static/img/game/baltoWalking${walkFrame}.png`; // Alterna imágenes
        }
    }

    setInterval(walkAnimation, 300); // Cambia de imagen cada 300ms

    function jump() {
        if (!isJumping) {
            isJumping = true;
            isWalking = false; // Detener la animación de caminar
            dogImg.src = `/static/img/game/baltoJumps.png`; // Imagen de salto

            dog.classList.add("jump");

            setTimeout(() => {
                dog.classList.remove("jump");
                isJumping = false;
                isWalking = true; // Reanudar animación de caminar
            }, 700); // Aumentamos el tiempo para que coincida con la animación
        }
    }

    document.addEventListener("keydown", (event) => {
        if (event.code === "Space" || event.key === "ArrowUp") {
            jump();
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    // Obtén el contenedor del fondo
    const background = document.getElementById("background");

    let backgroundPosition = 0;
    let speed = 0.2; // Velocidad de movimiento del fondo

    // Mover el fondo con una animación
    function moveBackground() {
        backgroundPosition -= speed; // Mueve el fondo hacia la izquierda
        background.style.backgroundPosition = `${backgroundPosition}px 0`; // Actualiza la posición
        requestAnimationFrame(moveBackground); // Continuar moviendo el fondo
    }

    moveBackground(); // Inicia el movimiento del fondo
});

