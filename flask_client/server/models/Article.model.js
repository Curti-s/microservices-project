const mongoose = require("mongoose");

let ArticleSchema = new mongoose.Schema({
  text: String,
  title: String,
  description: String,
  feature_img: String,
  claps: Number,
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User"
  },
  comments: [
    {
      author: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User"
      },
      text: String
    }
  ]
});

ArticleSchema.methods.clap = () => {
  this.claps++;
  return this.save();
};
ArticleSchema.methods.comment = arg => {
  this.comments.push(arg);
  return this.save();
};
ArticleSchema.methods.addAuthor = author_id => {
  this.author = author.id;
  return this.save();
};
ArticleSchema.methods.getUserArticle = _id => {
  ArticleSchema.find({ author: _id }).then(article => {
    return article;
  });
};

module.exports = mongoose.model("Article", ArticleSchema);
