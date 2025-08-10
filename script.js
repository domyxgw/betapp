// Symulowane dane meczów
const matches = [
  { home: "Real Madrid", away: "Barcelona", odds: 2.1, chance: 65 },
  { home: "Liverpool", away: "Manchester City", odds: 3.4, chance: 48 },
  { home: "PSG", away: "Marseille", odds: 1.8, chance: 72 },
  { home: "Juventus", away: "Inter", odds: 2.5, chance: 55 }
];

// Funkcja do generowania rekomendacji
function getRecommendation(chance) {
  if (chance >= 60) return "Warto obstawić";
  if (chance >= 50) return "Można rozważyć";
  return "Nie polecam";
}

// Wstawianie danych do tabeli
function renderMatches() {
  const table = document.getElementById("matches-table");
  table.innerHTML = "";

  matches.forEach(m => {
    const row = document.createElement("tr");
    if (m.chance >= 60) row.classList.add("recommended");

    row.innerHTML = `
      <td>${m.home} vs ${m.away}</td>
      <td>${m.odds}</td>
      <td>${m.chance}%</td>
      <td>${getRecommendation(m.chance)}</td>
    `;
    table.appendChild(row);
  });
}

renderMatches();
