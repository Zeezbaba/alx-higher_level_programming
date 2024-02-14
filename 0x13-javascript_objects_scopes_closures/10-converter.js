#!/usr/bin/node

exports.converter = function (base) {
  function baseConverter (num) {
    return num.toString(base);
  }
  return baseConverter;
};
