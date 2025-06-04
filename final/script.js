const form = document.getElementById('dogForm');
const breedList = document.getElementById('breedList');

// Dog breed data with images
const dogBreeds = [
  {
    name: "Golden Retriever",
    size: "large",
    energy: "high",
    kids: "yes",
    image: "golden_r.jpeg"
  },
  {
    name: "Labrador Retriever",
    size: "large",
    energy: "high",
    kids: "yes",
    image: "labra.jpeg"
  },
  {
    name: "Bulldog",
    size: "medium",
    energy: "low",
    kids: "yes",
    image: "bull_d.jpeg"
  },
  {
    name: "Beagle",
    size: "medium",
    energy: "medium",
    kids: "yes",
    image: "beagle_d.jpeg"
  },
  {
    name: "Chihuahua",
    size: "small",
    energy: "medium",
    kids: "no",
    image: "chichi_d.jpeg"
  },
  {
    name: "Shih Tzu",
    size: "small",
    energy: "low",
    kids: "yes",
    image: "tzu.jpeg"
  },
  {
    name: "Border Collie",
    size: "medium",
    energy: "high",
    kids: "yes",
    image: "collie.jpeg"
  },
  {
    name: "Poodle",
    size: "medium",
    energy: "medium",
    kids: "yes",
    image: ""
  },
  {
    name: "German Shepherd",
    size: "large",
    energy: "high",
    kids: "yes",
    image: "German_s.jpeg"
  },
  {
    name: "Cocker Spaniel",
    size: "medium",
    energy: "medium",
    kids: "yes",
    image: "spain_r.jpeg"
  }
];

// Handle form submission
form.addEventListener('submit', function (e) {
  e.preventDefault();

  const size = form.elements['size'].value;
  const energy = form.elements['energy'].value;
  const kids = form.elements['kids'].value;

  // Filter breeds based on input
  const matches = dogBreeds.filter(breed =>
    breed.size === size &&
    breed.energy === energy &&
    breed.kids === kids
  );

  breedList.innerHTML = ""; // Clear previous results

  if (matches.length === 0) {
    breedList.innerHTML = "<li>No breeds match your criteria. Try different options.</li>";
    return;
  }

  matches.slice(0, 4).forEach(breed => {
    const li = document.createElement('li');
    li.className = 'breed-card';

    const img = document.createElement('img');
    img.src = breed.image;
    img.alt = breed.name;

    const name = document.createElement('h3');
    name.textContent = breed.name;

    li.appendChild(img);
    li.appendChild(name);

    breedList.appendChild(li);
  });
});
