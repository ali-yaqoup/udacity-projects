import { task, src, dest, watch, series } from 'gulp';
import shell from 'gulp-shell';

// Default task to build and run Parcel
task('default', shell.task(['npx parcel index.html']));

// Test task to run Mocha unit tests
task('test', shell.task(['npx mocha test/**/*.js']));

// Cypress test task
task('cypress', shell.task(['npx cypress run']));

// Watch task for development
task('watch', () => {
    watch(['src/**/*.js', 'src/**/*.css', 'index.html'], series('default'));
});

// Build task for production
task('build', shell.task(['npx parcel build index.html']));

// Run all tests
task('test-all', series('test', 'cypress'));
