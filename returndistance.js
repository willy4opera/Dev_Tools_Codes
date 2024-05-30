// Function to calculate the distance between two points using the Haversine formula
function calculateDistance(lat1, lon1, lat2, lon2) {
    // Convert degrees to radians
    function toRadians(degrees) {
        return degrees * (Math.PI / 180);
    }

    const R = 6371; // Earth's radius in kilometers

    const dLat = toRadians(lat2 - lat1);
    const dLon = toRadians(lon2 - lon1);

    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    const distance = R * c; // Distance in kilometers

    return distance;
}

// Example usage:
const user1 = { lat: 52.5200, lon: 13.4050 }; // Berlin
const user2 = { lat: 48.8566, lon: 2.3522 };  // Paris

const distance = calculateDistance(user1.lat, user1.lon, user2.lat, user2.lon);

console.log(`The distance between the two users is ${distance.toFixed(2)} kilometers.`);
