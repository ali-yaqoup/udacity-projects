describe('Navigation tests', () => {
  beforeEach(() => {
    // Visit the application before each test
    cy.visit('http://localhost:1234');
  });

  it('should navigate to Card Set page when clicking "Card Set" in side menu', () => {
    // Click on "Card Set" link
    cy.get('[data-cy="nav-card-sets"]').click();
    
    // Verify that the card sets page is displayed
    cy.get('#card-sets').should('be.visible');
    cy.get('#card-sets').should('have.class', 'active');
    
    // Verify that other pages are not active
    cy.get('#home').should('not.have.class', 'active');
    cy.get('#about').should('not.have.class', 'active');
    
    // Verify card sets container is present
    cy.get('#card-sets-container').should('be.visible');
    cy.get('[data-cy="create-set-btn"]').should('be.visible');
  });

  it('should navigate to About page when clicking "About" in side menu', () => {
    // Click on "About" link
    cy.get('[data-cy="nav-about"]').click();
    
    // Verify that the about page is displayed
    cy.get('#about').should('be.visible');
    cy.get('#about').should('have.class', 'active');
    
    // Verify that other pages are not active
    cy.get('#home').should('not.have.class', 'active');
    cy.get('#card-sets').should('not.have.class', 'active');
    
    // Verify about content is present
    cy.get('.aboutContainer').should('be.visible');
    cy.get('.aboutContainer h1').should('contain', 'About');
  });

  it('should navigate to Home page when clicking "Home" in side menu', () => {
    // First navigate to another page
    cy.get('[data-cy="nav-about"]').click();
    
    // Then click on "Home" link
    cy.get('[data-cy="nav-home"]').click();
    
    // Verify that the home page is displayed
    cy.get('#home').should('be.visible');
    cy.get('#home').should('have.class', 'active');
    
    // Verify that other pages are not active
    cy.get('#card-sets').should('not.have.class', 'active');
    cy.get('#about').should('not.have.class', 'active');
    
    // Verify home content is present
    cy.get('#home h1').should('contain', 'Welcome to Card Game');
  });

  it('should show only one active page at a time', () => {
    // Start on home page
    cy.get('#home').should('have.class', 'active');
    
    // Navigate to card sets
    cy.get('[data-cy="nav-card-sets"]').click();
    cy.get('#card-sets').should('have.class', 'active');
    cy.get('#home').should('not.have.class', 'active');
    cy.get('#about').should('not.have.class', 'active');
    
    // Navigate to about
    cy.get('[data-cy="nav-about"]').click();
    cy.get('#about').should('have.class', 'active');
    cy.get('#home').should('not.have.class', 'active');
    cy.get('#card-sets').should('not.have.class', 'active');
  });
});
