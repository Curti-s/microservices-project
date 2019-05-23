const user = require("./User.route.js");
const article = require("./Article.route.js");

module.exports = router => {
  user(router);
  article(router);
};
