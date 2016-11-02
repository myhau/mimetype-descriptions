/* old simple js - too lazy to setup heavy gulp/webpack crap */

var mimeMap = require("./mimetype-descriptions-map.js");

// omg what is this

function pluck(o, prop) {
  if(!o || !o[prop]) {
    return {
      v: undefined,
      pluck: function() { return pluck(); }
    }
  } else {
    return {
      v: o[prop],
      pluck: function(prop2) { return pluck(o[prop], prop2); }
    }
  }
}

function pluckMime(prop) {
  return pluck(mimeMap, prop);
}

module.exports = {
  description: function(mimeName, lang) {
    if(!lang) {
      lang = "en";
    }
    return pluckMime(mimeName).pluck("description").pluck(lang).v;
  },
  icon: function(mimeName) {
    return pluckMime(mimeName).pluck("icon").v;
  },
  acronym: function(mimeName) {
    return pluckMime(mimeName).pluck("acronym").v;
  },
  expanded: function(mimeName) {
    return pluckMime(mimeName).pluck("expanded").v;
  },
  full: function(mimeName) {
    return mimeMap[mimeName];
  }
};