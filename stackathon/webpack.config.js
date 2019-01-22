module.exports = {
  entry: [
    '@babel/polyfill',
    './frontend/src/index.js'
  ],
  output: {
    path: __dirname,
    filename: './frontend/static/main.js'
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      }
    ]
  }
}
