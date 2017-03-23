var gulp = require('gulp'),
  connect = require('gulp-connect');
 
gulp.task('webserver', function() {
  connect.server({
  	root:__dirname,
    livereload: true
  });
});

gulp.task('default', ['webserver']);