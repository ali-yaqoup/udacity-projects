import { shuffle } from './Shuffle.js';
import { renderCardSets, showModal, hideModal, showError } from './utilityRenderFunctions.js';

// Application state
let cardSets = [
    {
        name: 'Sample Set',
        cards: [
            { front: 'Question 1', back: 'Answer 1' },
            { front: 'Question 2', back: 'Answer 2' },
            { front: 'Question 3', back: 'Answer 3' }
        ]
    }
];

let currentCardSet = null;

// DOM elements
const pages = document.querySelectorAll('.page');
const navLinks = document.querySelectorAll('nav a');
const cardSetsContainer = document.getElementById('card-sets-container');
const createSetBtn = document.getElementById('create-set-btn');
const createSetModal = document.getElementById('create-set-modal');
const createSetForm = document.getElementById('create-set-form');
const addCardModal = document.getElementById('add-card-modal');
const addCardForm = document.getElementById('add-card-form');

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    setupNavigation();
    setupModals();
    setupForms();
    renderCardSets(cardSetsContainer, cardSets);
});

// Navigation setup
function setupNavigation() {
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            showPage(targetId);
        });
    });
}

// Show specific page
function showPage(pageId) {
    pages.forEach(page => {
        page.classList.remove('active');
    });
    
    const targetPage = document.getElementById(pageId);
    if (targetPage) {
        targetPage.classList.add('active');
    }
}

// Modal setup
function setupModals() {
    // Close modals when clicking on X
    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.addEventListener('click', (e) => {
            const modal = e.target.closest('.modal');
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });
    
    // Close modals when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    });
}

// Form setup
function setupForms() {
    // Create Set form
    createSetForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const setNameInput = document.getElementById('set-name');
        const setName = setNameInput.value.trim();
        
        if (!setName) {
            showError('create-set-error', 'Set name cannot be empty');
            return;
        }
        
        const newSet = {
            name: setName,
            cards: []
        };
        
        cardSets.push(newSet);
        renderCardSets(cardSetsContainer, cardSets);
        
        createSetForm.reset();
        hideModal('create-set-modal');
        showPage('card-sets');
    });
    
    // Add Card form
    addCardForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const frontInput = document.getElementById('card-front');
        const backInput = document.getElementById('card-back');
        const front = frontInput.value.trim();
        const back = backInput.value.trim();
        
        if (!front || !back) {
            showError('add-card-error', 'Both card front and back cannot be empty');
            return;
        }
        
        if (currentCardSet) {
            currentCardSet.cards.push({ front, back });
            renderCardSets(cardSetsContainer, cardSets);
        }
        
        addCardForm.reset();
        hideModal('add-card-modal');
    });
    
    // Create Set button
    createSetBtn.addEventListener('click', () => {
        showModal('create-set-modal');
    });
}

// Make functions globally accessible for HTML event handlers
window.showAddCardModal = function(cardSet) {
    currentCardSet = cardSet;
    showModal('add-card-modal');
};

window.showModal = showModal;
window.hideModal = hideModal;
