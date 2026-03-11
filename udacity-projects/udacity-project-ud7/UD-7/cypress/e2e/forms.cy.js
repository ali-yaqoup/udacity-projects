describe('Forms tests', () => {
  beforeEach(() => {
    // Visit the application before each test
    cy.visit('http://localhost:1234');
    
    // Navigate to card sets page
    cy.get('[data-cy="nav-card-sets"]').click();
  });

  describe('Create Set Form', () => {
    beforeEach(() => {
      // Click on "Create New Set" button to open the modal
      cy.get('[data-cy="create-set-btn"]').click();
      cy.get('#create-set-modal').should('be.visible');
    });

    it('should create a new set with valid input (happy path)', () => {
      const setName = 'Test Card Set';
      
      // Fill in the form with valid data
      cy.get('[data-cy="set-name-input"]').type(setName);
      
      // Submit the form
      cy.get('[data-cy="create-set-submit"]').click();
      
      // Verify the modal is closed
      cy.get('#create-set-modal').should('not.be.visible');
      
      // Verify the new card set is created
      cy.get('#card-sets-container').should('contain', setName);
      
      // Verify no error message is shown
      cy.get('[data-cy="create-set-error"]').should('not.be.visible');
    });

    it('should show error when submitting empty set name (unhappy path)', () => {
      // Ensure modal is fully visible
      cy.get('#create-set-modal').should('be.visible');
      cy.get('[data-cy="set-name-input"]').should('be.visible');
      
      // Verify error element exists but is hidden initially
      cy.get('[data-cy="create-set-error"]').should('exist');
      cy.get('[data-cy="create-set-error"]').should('not.be.visible');
      
      // Submit form without entering any data using submit()
      cy.get('[data-cy="create-set-form"]').submit();
      
      // Wait a moment for the error to appear
      cy.wait(500);
      
      // Verify error message is displayed
      cy.get('[data-cy="create-set-error"]').should('be.visible');
      cy.get('[data-cy="create-set-error"]').should('contain', 'Set name cannot be empty');
      
      // Verify the modal remains open
      cy.get('#create-set-modal').should('be.visible');
      
      // Verify no new card set is created
      cy.get('#card-sets-container').should('not.contain', 'Test Card Set');
    });

    it('should show error when submitting whitespace-only set name (unhappy path)', () => {
      // Fill in the form with only whitespace
      cy.get('[data-cy="set-name-input"]').type('   ');
      
      // Submit the form
      cy.get('[data-cy="create-set-submit"]').click();
      
      // Verify error message is displayed with longer timeout
      cy.get('[data-cy="create-set-error"]', { timeout: 5000 }).should('be.visible');
      cy.get('[data-cy="create-set-error"]').should('contain', 'Set name cannot be empty');
      
      // Verify the modal remains open
      cy.get('#create-set-modal').should('be.visible');
    });

    it('should close modal when clicking the close button', () => {
      // Click the close button
      cy.get('#create-set-modal .close').click();
      
      // Verify the modal is closed
      cy.get('#create-set-modal').should('not.be.visible');
    });
  });

  describe('Add Card Form', () => {
    beforeEach(() => {
      // First create a test set to add cards to
      cy.get('[data-cy="create-set-btn"]').click();
      cy.get('[data-cy="set-name-input"]').type('Test Set for Cards');
      cy.get('[data-cy="create-set-submit"]').click();
      
      // Click on "Add Card" button to open the modal
      cy.get('[data-cy="add-card-btn-0"]').click();
      cy.get('#add-card-modal').should('be.visible');
    });

    it('should add a new card with valid input (happy path)', () => {
      const cardFront = 'What is 2+2?';
      const cardBack = '4';
      
      // Fill in the form with valid data
      cy.get('[data-cy="card-front-input"]').type(cardFront);
      cy.get('[data-cy="card-back-input"]').type(cardBack);
      
      // Submit the form
      cy.get('[data-cy="add-card-submit"]').click();
      
      // Verify the modal is closed
      cy.get('#add-card-modal').should('not.be.visible');
      
      // Verify the new card is added (should be visible in the card set)
      cy.get('#card-sets-container').should('contain', cardFront);
      
      // Verify no error message is shown
      cy.get('[data-cy="add-card-error"]').should('not.be.visible');
    });

    it('should show error when submitting empty card front (unhappy path)', () => {
      // Fill in only the back field
      cy.get('[data-cy="card-back-input"]').type('Some answer');
      
      // Submit form using submit()
      cy.get('[data-cy="add-card-form"]').submit();
      
      // Wait a moment for the error to appear
      cy.wait(500);
      
      // Verify error message is displayed
      cy.get('[data-cy="add-card-error"]').should('be.visible');
      cy.get('[data-cy="add-card-error"]').should('contain', 'Both card front and back cannot be empty');
      
      // Verify the modal remains open
      cy.get('#add-card-modal').should('be.visible');
    });

    it('should show error when submitting empty card back (unhappy path)', () => {
      // Fill in only the front field
      cy.get('[data-cy="card-front-input"]').type('Some question');
      
      // Submit form using submit()
      cy.get('[data-cy="add-card-form"]').submit();
      
      // Wait a moment for the error to appear
      cy.wait(500);
      
      // Verify error message is displayed
      cy.get('[data-cy="add-card-error"]').should('be.visible');
      cy.get('[data-cy="add-card-error"]').should('contain', 'Both card front and back cannot be empty');
      
      // Verify the modal remains open
      cy.get('#add-card-modal').should('be.visible');
    });

    it('should show error when submitting both fields empty (unhappy path)', () => {
      // Submit form without entering any data using submit()
      cy.get('[data-cy="add-card-form"]').submit();
      
      // Wait a moment for the error to appear
      cy.wait(500);
      
      // Verify error message is displayed
      cy.get('[data-cy="add-card-error"]').should('be.visible');
      cy.get('[data-cy="add-card-error"]').should('contain', 'Both card front and back cannot be empty');
      
      // Verify the modal remains open
      cy.get('#add-card-modal').should('be.visible');
    });

    it('should close modal when clicking the close button', () => {
      // Click the close button
      cy.get('#add-card-modal .close').click();
      
      // Verify the modal is closed
      cy.get('#add-card-modal').should('not.be.visible');
    });
  });
});
