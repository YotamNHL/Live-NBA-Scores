/* Pulls the most updated data for the latest games the last 24 hours via the REST api flask server. */
const getLatestGames = () => {
    return fetch('http://localhost:5000/games')
    .then(res => res.json())
    .then(data => data);
} 

module.exports = {
    getLatestGames
}