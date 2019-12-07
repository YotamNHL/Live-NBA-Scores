const getLatestGames = () => {
    return fetch('http://localhost:5000/games')
    .then(res => res.json())
    .then(data => data);
} 

module.exports = {
    getLatestGames
}