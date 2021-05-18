const { merge } = require('webpack-merge')
const commonConfiguration = require('./webpack.common.js')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

// const path = require("path");
// const webpack = require('webpack');

// const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

module.exports = merge(
    commonConfiguration,
    {
        mode: 'production',
        plugins:
            [
                new CleanWebpackPlugin()

                // new webpack.optimize.UglifyJsPlugin({
                //     sourceMap: false,
                //     mangle: false,
                //     comments: false
                // })
            ]
    }
)
