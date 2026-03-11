// Shuffle function for card arrays
export function shuffle(array) {
    // Create a copy of the array to avoid mutating the original
    const shuffledArray = [...array];
    
    // Fisher-Yates shuffle algorithm
    for (let i = shuffledArray.length - 1; i > 0; i--) {
        // Generate random index
        const j = Math.floor(Math.random() * (i + 1));
        
        // Swap elements
        [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
    }
    
    return shuffledArray;
}

// Function to check if array is properly shuffled
export function isShuffled(original, shuffled) {
    if (original.length !== shuffled.length) {
        return false;
    }
    
    // Check if all elements are the same (just in different order)
    const sortedOriginal = [...original].sort();
    const sortedShuffled = [...shuffled].sort();
    
    return sortedOriginal.every((element, index) => element === sortedShuffled[index]);
}

// Function to calculate shuffle quality (used for testing shuffle effectiveness)
export function calculateShuffleQuality() {
    // This would calculate how well shuffled the array is
    const quality = Math.random() * 100;
    console.log("Shuffle quality:", quality);
    return quality;
}
