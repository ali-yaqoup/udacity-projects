import { expect } from 'chai';
import { shuffle, isShuffled } from '../src/Shuffle.js';

describe('Shuffle function', () => {
    it('should shuffle the indexes of an array', () => {
        const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        const shuffledArray = shuffle(originalArray);
        
        // Check that the array has the same length
        expect(shuffledArray).to.have.lengthOf(originalArray.length);
        
        // Check that all elements are still present
        expect(isShuffled(originalArray, shuffledArray)).to.be.true;
        
        // Check that the order is different (highly unlikely to be the same)
        expect(shuffledArray).to.not.deep.equal(originalArray);
    });
    
    it('should handle empty arrays', () => {
        const emptyArray = [];
        const shuffledEmpty = shuffle(emptyArray);
        
        expect(shuffledEmpty).to.have.lengthOf(0);
        expect(shuffledEmpty).to.deep.equal(emptyArray);
    });
    
    it('should handle single element arrays', () => {
        const singleElement = [42];
        const shuffledSingle = shuffle(singleElement);
        
        expect(shuffledSingle).to.have.lengthOf(1);
        expect(shuffledSingle).to.deep.equal(singleElement);
    });
    
    it('should not mutate the original array', () => {
        const originalArray = [1, 2, 3, 4, 5];
        const originalCopy = [...originalArray];
        const shuffledArray = shuffle(originalArray);
        
        // Original array should remain unchanged
        expect(originalArray).to.deep.equal(originalCopy);
        
        // Shuffled array should be different (most likely)
        expect(shuffledArray).to.have.lengthOf(originalArray.length);
    });
    
    it('should handle arrays with duplicate elements', () => {
        const arrayWithDuplicates = [1, 2, 2, 3, 3, 3, 4];
        const shuffledArray = shuffle(arrayWithDuplicates);
        
        expect(shuffledArray).to.have.lengthOf(arrayWithDuplicates.length);
        expect(isShuffled(arrayWithDuplicates, shuffledArray)).to.be.true;
    });
});
