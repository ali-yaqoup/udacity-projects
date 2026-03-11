# Card Game Application

A modern web application for creating and managing card sets with shuffle functionality.

## Features

- Create and manage card sets
- Add cards to sets with front/back content
- Shuffle cards within sets
- Responsive design with navigation
- Form validation
- Unit tests with Mocha and Chai
- End-to-end tests with Cypress

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Build Tools**: Parcel, Gulp
- **Testing**: Mocha, Chai, Cypress
- **Code Quality**: ESLint, Prettier

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

## Available Scripts

- `npm start` - Start development server with Parcel
- `npm run dev` - Start development server with watch mode
- `npm run build` - Build for production
- `npm test` - Run unit tests
- `npm run test:cypress` - Run Cypress E2E tests
- `npm run test:all` - Run all tests

## Development

### Running the Application

Start the development server:
```bash
npm start
```

The application will be available at `http://localhost:1234`

### Running Tests

#### Unit Tests
```bash
npm test
```

#### End-to-End Tests

First, start the development server in one terminal:
```bash
npm start
```

Then run Cypress tests in another terminal:
```bash
npm run test:cypress
```

Or run all tests:
```bash
npm run test:all
```

### Code Quality

#### ESLint
Run ESLint to check for code issues:
```bash
npx eslint src/
```

#### Prettier
Format code with Prettier (install VS Code extensions recommended):
```bash
npx prettier --write src/
```

## Project Structure

```
├── src/
│   ├── app.js                 # Main application logic
│   ├── Shuffle.js             # Shuffle functionality
│   ├── utilityRenderFunctions.js  # UI rendering utilities
│   └── styles.css             # Application styles
├── test/
│   └── shuffle.js             # Unit tests for shuffle function
├── cypress/
│   ├── e2e/
│   │   ├── navigation.cy.js   # Navigation E2E tests
│   │   └── forms.cy.js        # Form E2E tests
│   └── support/               # Cypress support files
├── gulpfile.js                # Gulp configuration
├── cypress.config.js          # Cypress configuration
├── eslint.config.js           # ESLint configuration
└── package.json               # Project configuration
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License
