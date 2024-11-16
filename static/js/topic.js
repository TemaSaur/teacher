const topics = document.querySelectorAll('[data-topic]')

topics.forEach(topicEl => {
	topicEl.onclick = () => {
		const topic = topicEl.textContent.substring(0, topicEl.textContent.length - 2);
		const results = document.querySelector(`[data-topic-results="${topic}"]`)
		topicEl.classList.toggle('active')
		results.classList.toggle('shown')
	}
})
