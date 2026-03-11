// Custom Cypress commands can be added here

// Example custom command:
// Cypress.Commands.add('login', (email, password) => { ... })

// Global beforeEach hook for common setup
beforeEach(() => {
  // Clear local storage before each test
  cy.clearLocalStorage();
  
  // Clear cookies before each test
  cy.clearCookies();
});
