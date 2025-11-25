const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class Parser {
    constructor(configPath) {
        this.configPath = configPath;
    }

    loadConfig() {
        try {
            const filePath = path.resolve(this.configPath);
            const fileContent = fs.readFileSync(filePath, 'utf8');
            return yaml.load(fileContent);
        } catch (error) {
            throw new Error(`Failed to load config: ${error.message}`);
        }
    }

    validateConfig(config) {
        if (!config || typeof config !== 'object') {
            throw new Error('Invalid configuration: config must be an object');
        }
        if (!config.resources || !Array.isArray(config.resources)) {
            throw new Error('Invalid configuration: resources must be an array');
        }
        return true;
    }

    parse() {
        const config = this.loadConfig();
        this.validateConfig(config);
        return config;
    }
}

module.exports = Parser;