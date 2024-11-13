"use strict";
const { createApp, ref } = Vue;

const app = Vue.createApp({
    data() {
        return {
            userInput: '',
            chatHistory: []
        };
    },
    methods: {
        sendMessage() {
            if (this.userInput.trim() !== '') {
                this.chatHistory.push(['human', this.userInput]);
                this.userInput = '';
                // 模拟AI回复
                setTimeout(() => {
                    this.chatHistory.push(['ai', 'This is a simulated response.']);
                }, 1000);
            }
        }
    }
});

app.mount('#app');
