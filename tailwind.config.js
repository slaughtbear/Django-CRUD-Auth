module.exports = {
  content: [
    './tasks/templates/**/*.html',  // Para templates de la aplicación tasks
    './templates/**/*.html',           // Para templates generales (si tienes)
    './tasks/static/src/**/*.css',   // Para cualquier CSS que esté en tu carpeta estática en tasks
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
