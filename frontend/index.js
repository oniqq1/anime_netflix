document.addEventListener("DOMContentLoaded", () => {
    const btnMain = document.getElementById("btn-main");
    const btnBackup = document.getElementById("btn-backup");
    const playerMain = document.getElementById("player-main");
    const playerBackup = document.getElementById("player-backup");

    btnMain.onclick = () => {
        btnMain.classList.add("active");
        btnBackup.classList.remove("active");
        playerMain.classList.add("active");
        playerBackup.classList.remove("active");
    };

    btnBackup.onclick = () => {
        btnBackup.classList.add("active");
        btnMain.classList.remove("active");
        playerBackup.classList.add("active");
        playerMain.classList.remove("active");
    };
});
