async function getCharName() {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
        if (!response.ok) {
            throw newError(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json()
        if (data && data.name) {
            return data.name;
        } else {
            throw new Error('Data not found');
        }
    } catch (err) {
        console.error(err)
    } 
    const listMovies = document = document.getElementById('listMovie');
    getFilms().then((movies) => {
        const moviesItems = movies.map((movie) => `<li>${movie.title}</li>`).join('');
        listMovies.innerHTML = moviesItems;
    })
}