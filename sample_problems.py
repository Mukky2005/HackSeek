# Sample problem statements for testing and demonstration
import random

# Templates for different problem domains
problem_templates = {
    # Computer Science and Engineering Categories
    "Artificial Intelligence Ethics": [
        """
        Design a framework for ensuring ethical AI decision-making in {application_domain}. The solution should 
        address issues of bias, transparency, accountability, and privacy. It should provide clear guidelines for 
        developers and organizational leaders while incorporating mechanisms for ongoing monitoring and improvement 
        of AI systems to prevent {primary_concern} and {secondary_concern}.
        """,
        """
        Develop a comprehensive approach to ethical AI governance for {organization_type} working in {industry_type}. 
        The solution should balance innovation with responsibility, provide practical tools for {stakeholder_type} 
        to identify and mitigate ethical risks, and include metrics to evaluate compliance with ethical standards.
        """,
        """
        Create a system to detect and mitigate bias in AI algorithms used in {critical_domain}. The solution should 
        work across different types of machine learning models, provide explainable results to non-technical stakeholders, 
        and enable continuous improvement through {monitoring_approach} without significantly impacting performance.
        """
    ],
    
    "Cybersecurity Threat Detection": [
        """
        Design a next-generation threat detection system that can identify and respond to sophisticated cyber attacks 
        in real-time. The solution should protect {system_type} from {attack_vector} attacks, minimize false positives, 
        integrate with existing security infrastructure, and provide actionable intelligence to security teams for 
        rapid response.
        """,
        """
        Develop an innovative approach to detecting zero-day vulnerabilities in {software_type} before they can be 
        exploited. The solution should combine {analysis_technique} with {intelligence_source} to provide early warning 
        of potential security threats and recommend specific mitigation strategies tailored to the organization's risk profile.
        """,
        """
        Create a behavioral-based security monitoring system for {organization_size} organizations that can detect 
        insider threats and advanced persistent threats. The solution should establish baselines of normal activity, 
        identify anomalous behavior using {detection_method}, and streamline the investigation process while maintaining 
        employee privacy and reducing alert fatigue.
        """
    ],
    
    "Cloud-Native Architecture": [
        """
        Design a cloud-native architecture for migrating legacy {application_type} applications to a modern, 
        scalable, and resilient infrastructure. The solution should minimize downtime during migration, optimize 
        cost efficiency, enable continuous delivery, and improve performance by at least {percentage}% compared 
        to the current system.
        """,
        """
        Develop a reference architecture for cloud-native applications that enables {organization_type} to 
        achieve {primary_goal} and {secondary_goal}. The solution should address challenges of service discovery, 
        state management, and observability while providing a clear implementation roadmap that accounts for 
        skill gaps and technology constraints.
        """,
        """
        Create a multi-cloud strategy for {business_type} that prevents vendor lock-in while maximizing the benefits 
        of cloud-native technologies. The solution should include patterns for workload distribution, data consistency, 
        identity management, and cost optimization across different cloud providers and on-premises infrastructure.
        """
    ],
    
    "DevOps Automation": [
        """
        Design an end-to-end DevOps pipeline for {application_type} applications that automates the entire software 
        delivery lifecycle. The solution should include infrastructure as code, continuous integration, continuous 
        deployment, and automated testing to reduce deployment time from {current_timeframe} to {target_timeframe} 
        while improving quality and consistency.
        """,
        """
        Develop a DevOps transformation strategy for {team_size} development teams working on {legacy_factor} systems. 
        The approach should address cultural, process, and tooling changes required to implement DevOps practices, 
        with clear metrics to measure success and identify areas for continuous improvement.
        """,
        """
        Create a set of automated quality gates and compliance checks for organizations in the {regulated_industry} 
        industry. The solution should ensure that all software changes meet security, performance, and regulatory 
        requirements without creating bottlenecks in the delivery pipeline or requiring manual intervention.
        """
    ],
    
    "Blockchain Applications": [
        """
        Design a blockchain-based solution to address {trust_issue} in the {industry_type} industry. The solution 
        should provide immutable records, transparent processes, and secure transactions while addressing challenges 
        of scalability, interoperability with existing systems, and regulatory compliance.
        """,
        """
        Develop a practical application of blockchain technology to create a trustless ecosystem for {transaction_type} 
        between {stakeholder1} and {stakeholder2}. The solution should eliminate the need for intermediaries, reduce 
        transaction costs by {percentage}%, and provide a clear value proposition that overcomes adoption barriers.
        """,
        """
        Create a framework for implementing private blockchain networks that balance transparency with confidentiality 
        for {organization_type}. The solution should address governance structure, consensus mechanisms appropriate for 
        the use case, and integration with external systems while ensuring performance meets business requirements.
        """
    ],
    
    "Big Data Analytics": [
        """
        Design a big data analytics platform that enables {organization_type} to extract actionable insights from 
        {data_volume} of structured and unstructured data. The solution should address data ingestion, processing, 
        storage, analysis, and visualization with particular focus on {primary_insight} and {secondary_insight}.
        """,
        """
        Develop a real-time analytics capability for processing {data_type} data streams to identify {pattern_type} 
        as they emerge. The solution should handle data at {velocity} scale, provide insights within {timeframe}, 
        and enable automated actions based on predefined criteria and machine learning models.
        """,
        """
        Create a comprehensive data strategy that transforms {organization_size} organizations into data-driven 
        enterprises. The approach should address data governance, quality, integration, analytics capabilities, 
        and organizational changes required to derive maximum value from data assets while maintaining compliance 
        with {regulation_type} regulations.
        """
    ],
    
    "Natural Language Processing": [
        """
        Design a natural language processing system capable of understanding and generating {language_type} 
        content for {application_purpose}. The solution should achieve accuracy levels of at least {percentage}%, 
        handle domain-specific terminology, and adapt to evolving language patterns without requiring constant retraining.
        """,
        """
        Develop an NLP-powered solution to extract structured information from {document_type} documents with 
        varying formats and quality. The system should identify key entities, relationships, and context with 
        high precision, transforming unstructured content into actionable data for {business_process} automation.
        """,
        """
        Create a multilingual conversation AI system for {industry_type} that can understand user intent, maintain 
        context across interactions, and provide helpful responses in natural language. The solution should handle 
        {conversation_challenge} gracefully and improve over time through {learning_mechanism}.
        """
    ],
    
    "Computer Vision": [
        """
        Design a computer vision system to {vision_task} in {environment_type} environments with {accuracy_requirement} 
        accuracy. The solution should work under varying lighting conditions, identify {object_type} objects, and 
        integrate with existing {system_type} systems to automate decision-making processes.
        """,
        """
        Develop an edge-based vision processing solution for {device_type} with limited computational resources. 
        The system should perform {vision_function} with minimal latency, optimize power consumption, and maintain 
        accuracy levels suitable for {vision_application_domain} applications.
        """,
        """
        Create a vision-based monitoring system for {industry_type} that can detect anomalies, predict failures, 
        and improve safety. The solution should process visual data from multiple camera types, distinguish between 
        normal variations and actual issues, and generate appropriate alerts or actions based on severity.
        """
    ],
    
    "Internet of Things": [
        """
        Design an IoT architecture for {environment_type} environments that connects {device_number} devices 
        to provide {primary_function} and {secondary_function}. The solution should address power constraints, 
        network reliability, security, and scalability while delivering actionable insights to stakeholders.
        """,
        """
        Develop an edge computing strategy for IoT deployments in {remote_factor} locations. The solution should 
        optimize the distribution of processing between edge devices and cloud resources, ensure data integrity 
        during connectivity disruptions, and enable local decision-making for time-critical applications.
        """,
        """
        Create a comprehensive IoT security framework that protects {device_type} devices throughout their 
        lifecycle. The approach should include secure provisioning, authentication, authorization, encryption, 
        vulnerability management, and incident response tailored to the constraints of IoT environments.
        """
    ],
    
    "Quantum Computing Applications": [
        """
        Identify and design practical applications of quantum computing for solving {problem_type} problems 
        in the {industry_type} industry. The solution should define algorithms appropriate for near-term 
        quantum hardware, quantify expected advantages over classical approaches, and outline a migration 
        path as quantum technologies mature.
        """,
        """
        Develop a hybrid quantum-classical computing approach to address {computational_challenge} that is 
        intractable with current systems. The solution should optimize problem decomposition between quantum 
        and classical processors, account for current hardware limitations, and demonstrate measurable improvements 
        in {performance_metric}.
        """,
        """
        Create a quantum-resistant security implementation for {system_type} that will protect against future 
        quantum computing threats. The solution should include cryptographic algorithms expected to withstand 
        quantum attacks, a transition strategy from current cryptography, and an approach to maintain security 
        as quantum computing capabilities evolve.
        """
    ],
    
    "Software Architecture Modernization": [
        """
        Design a strategy for modernizing monolithic {legacy_system} applications to a microservices architecture. 
        The approach should include decomposition patterns, data management strategies, API design principles, 
        and a phased implementation plan that allows for incremental modernization while maintaining business continuity.
        """,
        """
        Develop a reference architecture for event-driven systems that enable {organization_type} to achieve 
        {business_goal} through improved responsiveness and scalability. The solution should address event 
        sourcing, command query responsibility segregation, and eventual consistency challenges in complex 
        business domains.
        """,
        """
        Create a technical debt reduction framework for {codebase_size} codebases that balances addressing 
        architectural issues with delivering new features. The solution should include assessment methodologies, 
        prioritization techniques, refactoring strategies, and metrics to track progress and demonstrate business value.
        """
    ],
    
    "Mobile App Innovation": [
        """
        Design a next-generation mobile application architecture that enables {feature_type} experiences 
        across multiple platforms and device types. The solution should optimize development efficiency, 
        user experience consistency, performance, and maintainability while reducing time-to-market by {percentage}%.
        """,
        """
        Develop a mobile app strategy for {organization_type} that leverages emerging technologies such as 
        {technology1} and {technology2} to create competitive advantage. The approach should address user 
        needs, technical feasibility, integration with existing systems, and methods to measure success.
        """,
        """
        Create an offline-first mobile application framework for users in {connectivity_challenged} regions. 
        The solution should provide full functionality without network connectivity, efficiently synchronize 
        data when connections are available, and resolve conflicts according to business rules.
        """
    ],
    
    "Human-Computer Interaction": [
        """
        Design a natural user interface for {application_type} that reduces interaction friction and learning curves 
        for {user_type} users. The solution should incorporate {interaction_method} input, adapt to user preferences 
        and abilities, and deliver measurable improvements in task completion rates and user satisfaction.
        """,
        """
        Develop a framework for creating accessible interfaces that comply with {standard_name} standards while 
        maintaining engaging user experiences. The solution should address varying user abilities, provide 
        implementation guidelines for developers, and include testing methodologies to verify accessibility.
        """,
        """
        Create an adaptive user experience system that personalizes interfaces based on user behavior, preferences, 
        and context. The solution should apply machine learning to optimize navigation paths, content presentation, 
        and feature discovery without creating privacy concerns or confusing users with unpredictable changes.
        """
    ],
    
    "Database Optimization": [
        """
        Design a database architecture for {application_type} applications that handles {data_volume} of data 
        while maintaining query response times under {time_threshold}. The solution should address data modeling, 
        indexing strategies, partitioning, caching, and query optimization for complex analytical and transactional workloads.
        """,
        """
        Develop a polyglot persistence strategy for applications with diverse data storage requirements. 
        The approach should select appropriate database technologies for different data types and access patterns, 
        manage consistency across multiple data stores, and optimize performance for {primary_operation} operations.
        """,
        """
        Create a database migration framework for transitioning from {legacy_database} to {modern_database} with 
        minimal downtime and risk. The solution should include data mapping, transformation rules, validation methods, 
        performance testing, and rollback procedures to ensure business continuity throughout the migration.
        """
    ],
    
    "Network Security": [
        """
        Design a zero-trust network architecture for {organization_type} with {security_requirement} requirements. 
        The solution should implement the principle of least privilege, continuous validation, and micro-segmentation 
        while maintaining usability and performance for legitimate users and applications.
        """,
        """
        Develop a comprehensive network security monitoring system capable of detecting and responding to 
        advanced threats. The solution should analyze network traffic using {analysis_technique}, identify 
        malicious patterns, correlate events across multiple sources, and automate initial response actions 
        to contain potential breaches.
        """,
        """
        Create a secure remote access solution for {workforce_type} workforce that protects corporate resources 
        from unauthorized access and data leakage. The approach should include strong authentication, fine-grained 
        authorization, encryption, endpoint security validation, and monitoring without significantly impacting 
        user productivity.
        """
    ],
    
    "Distributed Systems": [
        """
        Design a distributed system architecture for {application_type} that maintains consistency, availability, 
        and partition tolerance according to business requirements. The solution should address data replication, 
        conflict resolution, failure detection, and recovery mechanisms while scaling horizontally to handle 
        {load_parameter} load.
        """,
        """
        Develop a strategy for implementing distributed transactions across microservices without tight coupling 
        or compromising scalability. The approach should consider patterns such as saga, two-phase commit, or 
        eventual consistency with compensating transactions based on {business_domain} requirements for data integrity.
        """,
        """
        Create a resilient distributed computing platform that continues functioning despite {failure_type} failures. 
        The solution should implement circuit breakers, bulkheads, timeouts, and retry mechanisms with exponential 
        backoff while providing observability into system health and automated remediation when possible.
        """
    ],
    
    "Machine Learning Operations": [
        """
        Design an MLOps framework for {organization_type} that streamlines the end-to-end machine learning lifecycle 
        from experimentation to production. The solution should address model development, training, validation, 
        deployment, monitoring, and governance with particular focus on reproducibility and regulatory compliance.
        """,
        """
        Develop a continuous delivery pipeline for machine learning models that reduces deployment time from 
        {current_timeframe} to {target_timeframe}. The approach should automate feature engineering, model training, 
        validation, A/B testing, and deployment while ensuring quality, performance, and explainability.
        """,
        """
        Create a model monitoring system that detects and addresses drift in production machine learning models. 
        The solution should track data distributions, model outputs, and business metrics to identify when retraining 
        is needed, quantify the impact of drift, and enable automated or human-in-the-loop interventions.
        """
    ],
    
    "Edge Computing": [
        """
        Design an edge computing architecture for {application_type} applications that processes data locally 
        to reduce latency, bandwidth usage, and cloud computing costs. The solution should optimize workload 
        distribution between edge devices and cloud resources, manage limited computing resources efficiently, 
        and ensure data consistency across distributed nodes.
        """,
        """
        Develop a strategy for deploying and managing machine learning models on {edge_device} devices with 
        {resource_constraint} constraints. The approach should address model optimization for edge deployment, 
        versioning, updates, monitoring, and fallback mechanisms when local processing is insufficient.
        """,
        """
        Create a framework for building resilient edge applications that continue functioning when connectivity 
        to the cloud is limited or unavailable. The solution should implement local data storage, processing 
        prioritization, synchronization protocols, and conflict resolution strategies appropriate for {industry_type} use cases.
        """
    ],
    
    "API Management": [
        """
        Design a comprehensive API management strategy for {organization_type} that enables digital ecosystems 
        through secure, scalable, and developer-friendly interfaces. The solution should address API design, 
        security, rate limiting, analytics, documentation, developer onboarding, and lifecycle management.
        """,
        """
        Develop an API gateway architecture that handles {request_volume} requests while ensuring consistency, 
        security, and performance. The approach should implement authentication, authorization, traffic management, 
        request transformation, and monitoring without becoming a single point of failure.
        """,
        """
        Create a framework for API versioning and deprecation that balances innovation with backward compatibility. 
        The solution should include strategies for communicating changes, managing multiple versions simultaneously, 
        transitioning consumers to newer versions, and eventually retiring obsolete APIs without disrupting systems.
        """
    ],
    
    "Augmented Reality Applications": [
        """
        Design an augmented reality solution for {industry_type} that overlays digital information onto the physical 
        world to improve {primary_process} and {secondary_process}. The system should achieve positioning accuracy 
        of {accuracy_level}, work in {environment_type} environments, and integrate with existing {data_source} systems.
        """,
        """
        Develop an AR experience that enables {user_type} to visualize and interact with {content_type} content 
        through mobile devices or headsets. The solution should optimize rendering performance, battery usage, 
        and user experience while providing intuitive interactions and addressing potential safety concerns.
        """,
        """
        Create a multi-user augmented reality framework for collaborative work in {spatial_context} environments. 
        The approach should enable shared AR experiences with synchronized content, real-time updates, persistent 
        anchors, and communication capabilities while working across different device types.
        """
    ],
    
    "Robotics Software": [
        """
        Design a robotics control system for {robot_type} robots performing {task_type} tasks in {environment_type} 
        environments. The solution should optimize path planning, obstacle avoidance, task scheduling, and failure 
        recovery while meeting safety and performance requirements.
        """,
        """
        Develop a perception framework that enables robots to understand and navigate complex, dynamic environments. 
        The approach should fuse data from multiple sensor types, identify relevant objects and features, build 
        and maintain environmental maps, and support decision-making with uncertainty management.
        """,
        """
        Create a robot programming interface that allows {user_type} without robotics expertise to define and 
        modify robot behaviors. The solution should abstract complex robotics concepts, provide visual programming 
        tools, simulation capabilities, and safety constraints while supporting customization for specific use cases.
        """
    ],
    
    "Virtual Reality Development": [
        """
        Design a virtual reality environment for {training_type} training that improves learning outcomes compared 
        to traditional methods. The solution should create immersive scenarios, track user performance, adapt 
        difficulty based on progress, and provide meaningful feedback while minimizing motion sickness and user fatigue.
        """,
        """
        Develop a framework for creating social VR experiences that enable meaningful interaction between 
        {user_number} simultaneous users. The approach should address avatar representation, spatial audio, 
        shared object manipulation, body language simulation, and network optimization for low-latency communication.
        """,
        """
        Create a cross-platform virtual reality development methodology that produces consistent experiences 
        across {headset_type} headsets. The solution should maximize code reuse, adapt to different input methods, 
        optimize performance for each platform's capabilities, and provide analytics to measure user engagement.
        """
    ],
    
    "Game Development": [
        """
        Design a game engine architecture for {game_genre} games that optimizes performance on {platform_type} 
        platforms. The solution should address rendering, physics, audio, input handling, asset management, 
        and memory optimization while providing tools that increase developer productivity.
        """,
        """
        Develop an AI system for non-player characters that creates challenging and realistic opponents or 
        companions in {game_type} games. The approach should implement decision-making, pathfinding, learning, 
        and adaptation while being computationally efficient and creating engaging player experiences.
        """,
        """
        Create a procedural content generation framework for producing {content_type} game content that 
        is diverse, balanced, and aligned with design intent. The solution should reduce content creation costs, 
        enable personalized experiences, and maintain quality standards while allowing designer control over outcomes.
        """
    ],
    
    "Autonomous Systems": [
        """
        Design a decision-making architecture for autonomous {vehicle_type} operating in {environment_type} 
        environments. The solution should optimize path planning, object detection and tracking, behavior prediction, 
        risk assessment, and real-time decision-making while ensuring safety and compliance with regulations.
        """,
        """
        Develop a perception system for autonomous vehicles that functions reliably in {challenging_condition} 
        conditions. The approach should fuse data from {sensor_type} sensors, identify and classify objects with 
        {accuracy_level}% accuracy, estimate position and motion, and detect potential hazards with sufficient warning time.
        """,
        """
        Create a validation and verification framework for autonomous system safety that identifies potential 
        failure modes and edge cases. The solution should combine simulation, controlled testing, and operational 
        data analysis to demonstrate system safety according to {standard_name} standards before deployment.
        """
    ],
    
    "Low-Code/No-Code Platforms": [
        """
        Design a low-code development platform that enables {user_type} to create enterprise-grade applications 
        for {application_purpose} without traditional programming. The solution should provide visual development 
        tools, pre-built templates, integration capabilities, and extension points for developers to add custom 
        functionality when needed.
        """,
        """
        Develop a strategy for implementing low-code platforms within {organization_type} that accelerates 
        application delivery while maintaining governance and quality. The approach should address citizen 
        developer enablement, professional developer collaboration, security controls, and sustainability of 
        applications beyond initial development.
        """,
        """
        Create a domain-specific low-code platform for building {application_type} applications in the 
        {industry_type} industry. The solution should encapsulate industry knowledge and best practices 
        in reusable components, validation rules, and workflows while allowing customization for specific 
        organizational requirements.
        """
    ],
    
    "Embedded Systems": [
        """
        Design an embedded software architecture for {device_type} devices with {resource_constraint} constraints. 
        The solution should optimize performance, power consumption, and reliability while providing update mechanisms, 
        security features, and interfaces for integration with other systems.
        """,
        """
        Develop a real-time operating system approach for embedded devices performing {critical_function} functions 
        with {timing_requirement} timing requirements. The solution should ensure deterministic behavior, efficient 
        resource utilization, fault tolerance, and certification compliance for {industry_type} applications.
        """,
        """
        Create a framework for secure communication between embedded devices in {deployment_scenario} scenarios. 
        The approach should implement lightweight encryption, authentication, secure boot, and intrusion detection 
        suitable for resource-constrained devices while addressing physical security vulnerabilities.
        """
    ],
    
    "Data Privacy Engineering": [
        """
        Design a privacy-preserving architecture for systems handling {data_type} data subject to {regulation_name} 
        regulations. The solution should implement privacy by design principles, data minimization, purpose limitation, 
        consent management, and audit capabilities while maintaining system functionality and performance.
        """,
        """
        Develop a framework for conducting privacy impact assessments and implementing appropriate controls 
        for {system_type} systems. The approach should identify privacy risks, recommend proportionate mitigation 
        measures, track compliance, and adapt to evolving regulations and threats to personal data.
        """,
        """
        Create a technical implementation of differential privacy that enables valuable analytics on sensitive 
        datasets while providing mathematical privacy guarantees. The solution should calibrate noise addition based 
        on sensitivity and privacy budget, track cumulative privacy loss, and maintain utility for {analytics_type} analytics.
        """
    ],
    
    "Parallel Computing": [
        """
        Design a parallel computing architecture for {computation_type} computations that scales efficiently 
        across {processor_number} processors. The solution should address data partitioning, load balancing, 
        communication optimization, synchronization, and fault tolerance while achieving near-linear speedup.
        """,
        """
        Develop a framework for parallelizing {algorithm_type} algorithms on heterogeneous computing platforms 
        combining CPUs, GPUs, and specialized accelerators. The approach should optimize workload distribution 
        based on processor characteristics, manage memory hierarchies efficiently, and adapt to different hardware configurations.
        """,
        """
        Create a high-performance computing solution for {scientific_domain} simulations requiring {computational_resource} 
        computational resources. The solution should implement domain decomposition, optimize inter-node communication, 
        provide checkpointing for long-running jobs, and include visualization capabilities for result analysis.
        """
    ],
    
    "Software Testing Automation": [
        """
        Design a comprehensive test automation strategy for {application_type} applications that reduces manual 
        testing effort by {percentage}% while improving coverage and reliability. The solution should address unit, 
        integration, API, UI, performance, and security testing with appropriate tools and frameworks for each level.
        """,
        """
        Develop a continuous testing approach integrated with CI/CD pipelines that provides rapid feedback on 
        code changes without becoming a bottleneck. The solution should optimize test selection, parallelization, 
        data management, environment provisioning, and results reporting to minimize cycle time while maintaining quality.
        """,
        """
        Create a test automation framework for {legacy_factor} systems with limited testability. The approach 
        should implement appropriate test patterns, service virtualization, data management, and reporting 
        capabilities while requiring minimal changes to the system under test.
        """
    ],
    
    "Compiler Design": [
        """
        Design a domain-specific language and compiler for {domain_type} applications that improves developer 
        productivity and program correctness. The solution should provide abstractions relevant to the domain, 
        static analysis capabilities, optimization opportunities, and integration with existing development tools.
        """,
        """
        Develop a compiler optimization framework that improves {performance_metric} for {language_type} programs 
        by {percentage}%. The approach should implement traditional and machine learning-based optimization 
        techniques, provide feedback to developers about optimization opportunities, and adapt to different 
        target architectures.
        """,
        """
        Create a source-to-source translation system for migrating applications from {legacy_language} to 
        {target_language}. The solution should preserve functionality, maintain code readability, handle 
        language idioms appropriately, and identify areas requiring manual intervention while accelerating 
        the overall migration process.
        """
    ],
    
    "Climate Change Mitigation": [
        """
        Develop an innovative solution to reduce carbon emissions in urban areas. The solution should be cost-effective, 
        scalable, and able to be implemented within existing city infrastructure. It should address transportation, 
        energy usage, or waste management, and should provide measurable results within {timeframe} of implementation.
        """,
        """
        Create a scalable approach to help {location_type} reduce their carbon footprint by at least {percentage}% 
        within the next {timeframe}. The solution should balance efficiency, cost, and ease of adoption, focusing 
        on {focus_area} while providing clear metrics to track progress.
        """,
        """
        Design a comprehensive strategy to combat climate change effects in {location_type}. The approach should 
        focus on {focus_area} and deliver quantifiable improvements in sustainability within {timeframe}. Consider 
        both technological innovation and behavioral change components.
        """
    ],
    
    "Remote Education Access": [
        """
        Create a system to provide quality education to students in remote areas with limited internet connectivity. 
        The solution should work with minimal infrastructure, be accessible on basic devices, and support both 
        synchronous and asynchronous learning. It should track student progress and provide meaningful feedback 
        to both students and teachers.
        """,
        """
        Develop an educational platform for {target_audience} in areas with {connectivity_level} connectivity. 
        The solution must function on {device_type} devices, support multiple learning modes, and effectively 
        measure learning outcomes despite infrastructure limitations.
        """,
        """
        Design an innovative approach to deliver high-quality education to {target_audience} in {location_type} 
        regions. The solution should overcome challenges related to {primary_challenge} and {secondary_challenge}, 
        while maintaining educational standards equivalent to well-resourced institutions.
        """
    ],
    
    "Healthcare Data Management": [
        """
        Design a secure and efficient system for managing and sharing healthcare data across different providers 
        while maintaining patient privacy. The solution should reduce administrative overhead, prevent duplicate 
        testing, improve diagnosis accuracy, and comply with relevant healthcare regulations. It must be user-friendly 
        for both healthcare providers and patients.
        """,
        """
        Create a healthcare data platform that addresses challenges of {primary_challenge} and {secondary_challenge} 
        in the medical information ecosystem. The system should prioritize data security while improving efficiency 
        for {stakeholder_group} by at least {percentage}%.
        """,
        """
        Develop a next-generation health information system that balances accessibility and privacy. The solution 
        should focus on improving outcomes for patients with {condition_type} conditions while reducing operational 
        costs by {percentage}% through enhanced data integration and analytics.
        """
    ],
    
    "Small Business Digital Transformation": [
        """
        Develop a cost-effective approach for small businesses to digitize their operations in the post-pandemic 
        economy. The solution should address online presence, digital payments, inventory management, and customer 
        relationship management. It should be accessible to non-technical users, require minimal upfront investment, 
        and provide clear ROI within 6 months.
        """,
        """
        Create a digital transformation framework for {business_type} with {employee_count} employees. The solution 
        should prioritize {primary_focus} and {secondary_focus}, require minimal technical expertise, and demonstrate 
        ROI within {timeframe}.
        """,
        """
        Design a streamlined approach for small businesses in the {industry_type} industry to adopt digital tools 
        that enhance {primary_benefit} and {secondary_benefit}. The solution should be implementable with limited 
        resources and generate measurable improvements within {timeframe}.
        """
    ],
    
    "Food Waste Reduction": [
        """
        Create an innovative system to reduce food waste in the supply chain from producers to consumers. 
        The solution should address issues of overproduction, inefficient distribution, poor inventory management, 
        or consumer behavior. It should be economically sustainable and provide incentives for all stakeholders 
        to participate. The goal is to reduce food waste by at least 30% in implemented areas.
        """,
        """
        Develop a comprehensive approach to minimize food waste at the {supply_chain_stage} stage of the food 
        supply chain. The solution should address challenges related to {primary_challenge} and reduce waste 
        by {percentage}% while creating economic benefits for {stakeholder_group}.
        """,
        """
        Design a scalable system to tackle food waste in {location_type} areas, focusing on the connection between 
        {stakeholder1} and {stakeholder2}. The approach should combine technology and process improvements to 
        reduce waste while creating new value streams from previously discarded food resources.
        """
    ],
    
    "Water Conservation": [
        """
        Design a solution to promote water conservation in residential areas experiencing drought conditions. 
        The approach should combine technology, behavior change, and possibly policy recommendations. It should 
        be affordable to implement, provide measurable results, and be adaptable to different housing types 
        and community sizes. The solution should aim to reduce water usage by at least 20% without significantly 
        impacting quality of life.
        """,
        """
        Create a water conservation system for {location_type} facing {water_issue_type} issues. The solution should 
        reduce water consumption by {percentage}% through a combination of {approach_type} strategies while remaining 
        accessible to communities with varying resource levels.
        """,
        """
        Develop an integrated approach to water conservation that addresses both immediate usage reduction and 
        long-term sustainability. The solution should focus on {primary_focus} applications in {location_type} 
        regions and deliver demonstrable improvements within {timeframe}.
        """
    ],
    
    "Mental Health Support": [
        """
        Develop an accessible system for providing mental health support to underserved communities. 
        The solution should address barriers such as stigma, cost, and limited access to professionals. 
        It should provide both preventative measures and intervention strategies, be culturally sensitive, 
        and maintain user privacy and confidentiality. The approach should leverage both technology and 
        community resources.
        """,
        """
        Create a mental health support framework for {target_population} facing barriers including {primary_barrier} 
        and {secondary_barrier}. The solution should blend {approach_type} methods with community engagement to 
        provide both crisis intervention and ongoing support.
        """,
        """
        Design an innovative mental health system that increases access for {target_population} by {percentage}%. 
        The approach should address cultural and economic factors specific to this population while leveraging 
        technology to extend the reach of limited professional resources.
        """
    ],
    
    "Smart City Traffic Management": [
        """
        Create an intelligent traffic management system to reduce congestion in urban areas. The solution 
        should utilize real-time data, optimize traffic flow, reduce average commute times, and lower 
        emissions from idling vehicles. It should integrate with existing infrastructure where possible 
        and provide clear, actionable information to city planners and commuters. The system should be 
        adaptable to cities of varying sizes and layouts.
        """,
        """
        Develop a next-generation traffic management platform for cities with {population_size} populations. 
        The system should reduce congestion by {percentage}% during peak hours while decreasing emissions 
        and integrating with {infrastructure_type} infrastructure.
        """,
        """
        Design a comprehensive solution to traffic management challenges in {city_type} urban environments. 
        The approach should balance immediate congestion reduction with long-term mobility planning, utilizing 
        data from {data_source_type} to optimize traffic patterns and commuter experience.
        """
    ]
}

# Variable options for template placeholders
variable_options = {
    # Original variables
    "timeframe": ["6 months", "1 year", "18 months", "2 years", "3 years", "5 years"],
    "percentage": ["15", "20", "25", "30", "40", "50"],
    "location_type": ["urban centers", "suburban communities", "rural areas", "developing regions", "coastal cities", "industrial zones", "agricultural communities"],
    "focus_area": ["renewable energy adoption", "sustainable transportation", "waste reduction", "resource efficiency", "circular economy models", "community engagement"],
    "target_audience": ["K-12 students", "university students", "adult learners", "vocational trainees", "underserved communities"],
    "connectivity_level": ["intermittent", "low-bandwidth", "limited", "unreliable", "satellite-dependent"],
    "device_type": ["basic smartphones", "tablets", "older computers", "low-cost devices", "shared computing resources"],
    "primary_challenge": ["data fragmentation", "legacy systems", "information security", "resource limitations", "technical complexity", "regulatory compliance"],
    "secondary_challenge": ["user adoption", "interoperability", "scalability", "cost constraints", "privacy concerns", "maintenance requirements"],
    "stakeholder_group": ["rural hospitals", "specialty clinics", "patients with chronic conditions", "emergency responders", "medical researchers"],
    "condition_type": ["chronic", "rare", "infectious", "pediatric", "geriatric", "preventable"],
    "business_type": ["retail shops", "restaurants", "service providers", "manufacturing businesses", "professional practices"],
    "employee_count": ["1-5", "5-10", "10-25", "under 50", "family-run"],
    "primary_focus": ["customer acquisition", "operational efficiency", "payment processing", "inventory management", "remote work capabilities"],
    "secondary_focus": ["brand awareness", "customer retention", "supply chain optimization", "financial management", "market analysis"],
    "industry_type": ["food service", "retail", "professional services", "manufacturing", "tourism", "construction"],
    "primary_benefit": ["customer engagement", "operational efficiency", "market reach", "service quality", "product development"],
    "secondary_benefit": ["cost reduction", "business intelligence", "employee satisfaction", "supply chain visibility", "competitive advantage"],
    "supply_chain_stage": ["production", "processing", "distribution", "retail", "consumption", "post-consumer"],
    "stakeholder1": ["farmers", "food processors", "distributors", "retailers", "restaurants", "consumers", "food banks"],
    "stakeholder2": ["grocers", "food service businesses", "institutional buyers", "community organizations", "waste management companies"],
    "water_issue_type": ["drought", "scarcity", "quality concerns", "infrastructure limitations", "rising costs"],
    "approach_type": ["technological", "behavioral", "policy-based", "educational", "community-driven", "incentive-based"],
    "target_population": ["adolescents", "elderly individuals", "low-income communities", "rural populations", "veterans", "minority groups"],
    "primary_barrier": ["stigma", "cost", "geographical access", "awareness", "cultural factors", "service availability"],
    "secondary_barrier": ["transportation", "digital literacy", "language barriers", "continuity of care", "family support"],
    "population_size": ["small (under 100,000)", "medium (100,000-500,000)", "large (500,000-1 million)", "metropolitan (over 1 million)"],
    "infrastructure_type": ["existing traffic light", "public transportation", "sensor-based", "connected vehicle", "smart road"],
    "city_type": ["rapidly growing", "historically congested", "tourist-heavy", "economically diverse", "geographically constrained"],
    "data_source_type": ["connected vehicles", "mobile devices", "traffic cameras", "environmental sensors", "public transit systems"],
    
    # CSE-specific variables
    "application_domain": ["healthcare", "finance", "criminal justice", "hiring and employment", "education", "social media", "autonomous systems"],
    "primary_concern": ["algorithmic bias", "privacy violations", "lack of explainability", "safety issues", "data misuse", "security vulnerabilities"],
    "secondary_concern": ["workforce displacement", "intellectual property challenges", "regulatory compliance", "liability questions", "digital divides"],
    "organization_type": ["technology startups", "enterprise corporations", "government agencies", "educational institutions", "research labs", "nonprofit organizations"],
    "stakeholder_type": ["developers", "project managers", "executives", "compliance officers", "end users", "data scientists"],
    "critical_domain": ["healthcare diagnostics", "financial services", "autonomous vehicles", "criminal justice", "hiring systems", "content moderation"],
    "monitoring_approach": ["regular audits", "diverse testing teams", "explainable AI tools", "community feedback", "continuous evaluation"],
    
    "system_type": ["cloud infrastructure", "IoT networks", "critical infrastructure", "enterprise networks", "financial systems", "healthcare systems"],
    "attack_vector": ["ransomware", "phishing", "supply chain", "zero-day", "insider threat", "DDoS", "advanced persistent threat"],
    "software_type": ["web applications", "mobile apps", "firmware", "operating systems", "industrial control systems", "custom enterprise software"],
    "analysis_technique": ["static code analysis", "dynamic testing", "fuzz testing", "penetration testing", "formal verification", "machine learning-based detection"],
    "intelligence_source": ["threat intelligence feeds", "open source intelligence", "darkweb monitoring", "security researcher community", "internal security data"],
    "organization_size": ["small businesses", "mid-size enterprises", "large corporations", "government institutions", "multinational organizations"],
    "detection_method": ["behavior analytics", "anomaly detection", "machine learning models", "threat intelligence correlation", "zero trust verification"],
    
    "application_type": ["monolithic", "microservices-based", "serverless", "containerized", "batch processing", "real-time streaming", "transactional", "analytical"],
    "primary_goal": ["horizontal scalability", "cost optimization", "developer productivity", "operational resilience", "continuous delivery", "regulatory compliance"],
    "secondary_goal": ["reduced time-to-market", "improved security posture", "better observability", "simplified operations", "vendor independence"],
    "current_timeframe": ["weeks", "days", "hours", "months", "quarters"],
    "target_timeframe": ["minutes", "hours", "1-2 days", "a single day", "under an hour"],
    
    "team_size": ["small (3-5 developers)", "medium (5-15 developers)", "large (15-50 developers)", "enterprise (50+ developers)"],
    "legacy_factor": ["decades-old", "poorly documented", "tightly coupled", "heavily customized", "performance-critical"],
    "regulated_industry": ["healthcare", "finance", "government", "critical infrastructure", "telecommunications", "energy"],
    
    "trust_issue": ["supply chain traceability", "intellectual property protection", "digital identity verification", "contractual compliance", "multi-party trust"],
    "transaction_type": ["digital rights management", "cross-border payments", "property transfers", "credential verification", "supply chain documentation"],
    
    "data_volume": ["terabytes", "petabytes", "exabytes", "millions of records", "billions of events"],
    "primary_insight": ["customer behavior patterns", "operational inefficiencies", "fraud indicators", "market trends", "risk factors"],
    "secondary_insight": ["competitive intelligence", "predictive maintenance opportunities", "supply chain optimization", "customer churn prediction", "resource allocation"],
    "data_type": ["sensor", "transactional", "social media", "video", "audio", "text", "geospatial"],
    "pattern_type": ["anomalies", "trends", "correlations", "causality indicators", "behavioral shifts", "emerging clusters"],
    "velocity": ["millions of events per second", "hundreds of thousands of transactions per minute", "real-time streaming", "batch processing"],
    "regulation_type": ["GDPR", "CCPA", "HIPAA", "PCI DSS", "industry-specific"],
    
    "language_type": ["conversational", "technical", "creative", "multilingual", "domain-specific", "emotional", "persuasive"],
    "application_purpose": ["customer service", "content generation", "summarization", "translation", "sentiment analysis", "knowledge extraction"],
    "document_type": ["legal contracts", "medical records", "financial statements", "technical documentation", "unstructured reports", "forms and applications"],
    "business_process": ["claims processing", "customer onboarding", "compliance checking", "resume screening", "content moderation"],
    "conversation_challenge": ["ambiguous queries", "context switching", "emotional situations", "specialized knowledge requirements", "multi-turn interactions"],
    "learning_mechanism": ["supervised fine-tuning", "reinforcement learning from user feedback", "continuous knowledge base updates", "federated learning"],
    
    "vision_task": ["detect manufacturing defects", "recognize human activities", "monitor environmental changes", "identify security threats", "track inventory", "assist navigation"],
    "environment_type": ["industrial", "urban", "indoor", "outdoor", "low-light", "dynamic", "controlled", "challenging weather", "underwater"],
    "accuracy_requirement": ["99.9%", "95%", "90% or better", "human-level", "mission-critical"],
    "object_type": ["industrial components", "human subjects", "vehicles", "products", "infrastructure elements", "natural features"],
    "vision_function": ["object detection", "image classification", "semantic segmentation", "activity recognition", "optical character recognition", "3D reconstruction"],
    "vision_application_domain": ["manufacturing", "retail", "security", "healthcare", "agriculture", "autonomous vehicles", "augmented reality"],
    
    "device_number": ["hundreds", "thousands", "tens of thousands", "millions", "billions"],
    "primary_function": ["environmental monitoring", "asset tracking", "predictive maintenance", "process automation", "safety monitoring"],
    "secondary_function": ["energy optimization", "inventory management", "quality control", "security surveillance", "customer experience enhancement"],
    "remote_factor": ["geographically isolated", "connectivity-challenged", "harsh environmental", "physically secured", "power-limited"],
    
    "problem_type": ["optimization", "simulation", "cryptographic", "machine learning", "financial modeling", "materials science"],
    "computational_challenge": ["protein folding", "cryptographic security", "complex system simulation", "optimization at scale", "material design"],
    "performance_metric": ["solution quality", "computational time", "energy efficiency", "accuracy", "problem scale"],
    
    "legacy_system": ["mainframe-based", "monolithic", "client-server", "custom-developed", "ERP", "CRM"],
    "business_goal": ["agility", "scalability", "reliability", "innovation acceleration", "cost reduction", "customer experience improvement"],
    "codebase_size": ["small (under 100K LOC)", "medium (100K-1M LOC)", "large (over 1M LOC)", "distributed (multiple repositories)"],
    
    "feature_type": ["offline-first", "augmented reality", "real-time collaborative", "location-aware", "machine learning-powered", "accessibility-focused"],
    "technology1": ["augmented reality", "machine learning", "blockchain", "edge computing", "biometric authentication", "voice interfaces"],
    "technology2": ["cross-platform frameworks", "serverless backends", "progressive web apps", "real-time collaboration", "embedded analytics"],
    "connectivity_challenged": ["rural", "developing", "travel-heavy", "field service", "disaster-affected"],
    
    "user_type": ["elderly", "technical", "non-technical", "accessibility-dependent", "field workers", "busy professionals", "children"],
    "interaction_method": ["voice", "touch", "gesture", "eye tracking", "brain-computer interface", "multimodal"],
    "standard_name": ["WCAG 2.1", "Section 508", "ADA", "ISO 9241", "platform-specific accessibility guidelines"],
    
    "time_threshold": ["10ms", "50ms", "100ms", "500ms", "1 second"],
    "legacy_database": ["mainframe databases", "relational databases", "file-based storage", "proprietary databases", "first-generation NoSQL"],
    "modern_database": ["cloud-native databases", "distributed NoSQL", "NewSQL", "time-series databases", "graph databases", "search engines"],
    "primary_operation": ["read", "write", "query", "analytics", "transaction processing", "search", "aggregation"],
    
    "security_requirement": ["government", "financial", "healthcare", "defense", "critical infrastructure", "data protection"],
    "workforce_type": ["hybrid", "fully remote", "contractor-heavy", "bring-your-own-device", "field", "global"],
    
    "load_parameter": ["peak", "sustained high", "variable", "unpredictable", "growing", "periodic spike"],
    "business_domain": ["financial", "e-commerce", "inventory management", "customer management", "subscription services"],
    "failure_type": ["node", "network", "datacenter", "region", "service dependency", "data corruption"],
    
    "edge_device": ["smartphones", "IoT sensors", "smart cameras", "industrial controllers", "consumer electronics", "autonomous vehicles"],
    "resource_constraint": ["memory", "processing power", "battery life", "network bandwidth", "storage", "thermal"],
    
    "request_volume": ["millions per day", "thousands per second", "billions per month", "highly variable", "steadily growing"],
    
    "accuracy_level": ["millimeter", "centimeter", "sub-meter", "room-level", "building-level"],
    "data_source": ["CRM", "ERP", "IoT", "legacy systems", "third-party APIs", "real-time sensors", "CAD/BIM"],
    "primary_process": ["maintenance procedures", "customer navigation", "surgical guidance", "training", "quality assurance"],
    "secondary_process": ["documentation", "remote collaboration", "error reduction", "compliance verification", "knowledge transfer"],
    "content_type": ["3D models", "procedural instructions", "navigational guidance", "contextual data", "interactive simulations"],
    "spatial_context": ["office", "industrial", "educational", "medical", "retail", "field service"],
    
    "robot_type": ["industrial", "service", "mobile", "collaborative", "aerial", "underwater"],
    "task_type": ["assembly", "inspection", "material handling", "human assistance", "exploration", "maintenance"],
    
    "training_type": ["safety", "medical", "technical skills", "soft skills", "emergency response", "procedural"],
    "user_number": ["2-5", "5-20", "20-50", "50+", "hundreds", "thousands"],
    "headset_type": ["tethered PC", "standalone", "smartphone-based", "enterprise", "consumer", "mixed reality"],
    
    "game_genre": ["action", "adventure", "strategy", "simulation", "role-playing", "puzzle", "educational"],
    "platform_type": ["mobile", "console", "PC", "VR/AR", "cross-platform", "web-based"],
    "game_type": ["competitive multiplayer", "cooperative", "single-player narrative", "open world", "procedural"],
    "game_content_type": ["levels", "characters", "quests", "environments", "items", "narratives"],
    
    "vehicle_type": ["ground", "aerial", "underwater", "industrial", "personal transport", "logistics"],
    "challenging_condition": ["nighttime", "adverse weather", "heavy traffic", "off-road", "GPS-denied", "crowded urban"],
    "sensor_type": ["camera", "LiDAR", "radar", "ultrasonic", "GPS", "inertial", "multispectral"],
    
    "application_purpose": ["internal business operations", "customer-facing services", "data analysis", "process automation", "content management"],
    
    "critical_function": ["safety-critical", "real-time control", "monitoring", "communication", "data acquisition"],
    "timing_requirement": ["hard real-time", "soft real-time", "millisecond", "microsecond", "deterministic"],
    "deployment_scenario": ["industrial", "consumer", "medical", "automotive", "aerospace", "energy"],
    
    "data_type": ["personal", "biometric", "financial", "location", "behavioral", "health", "communications"],
    "regulation_name": ["GDPR", "CCPA", "HIPAA", "FERPA", "GLBA", "industry-specific"],
    "analytics_type": ["demographic", "behavioral", "predictive", "risk", "performance", "operational"],
    
    "computation_type": ["scientific simulation", "financial modeling", "AI training", "data processing", "rendering", "signal processing"],
    "processor_number": ["dozens", "hundreds", "thousands", "tens of thousands", "millions"],
    "algorithm_type": ["numerical", "graph", "matrix", "search", "optimization", "machine learning"],
    "scientific_domain": ["climate", "molecular dynamics", "fluid dynamics", "genomics", "material science", "astronomy"],
    "computational_resource": ["petaflop", "exaflop", "cluster", "supercomputer", "GPU array", "distributed"],
    
    "legacy_factor": ["poorly documented", "complex", "business-critical", "rapidly changing", "performance-sensitive"],
    
    "domain_type": ["financial", "scientific", "engineering", "data processing", "system programming", "web development"],
    "performance_metric": ["execution speed", "memory usage", "energy efficiency", "code size", "startup time"],
    "language_type": ["procedural", "object-oriented", "functional", "scripting", "statically typed", "dynamically typed"],
    "legacy_language": ["COBOL", "Fortran", "Visual Basic", "C", "Pascal", "Assembly"],
    "target_language": ["Java", "Python", "C#", "Rust", "Go", "JavaScript", "TypeScript"]
}

def generate_problem(category):
    """Generate a unique problem statement for the given category"""
    
    # Select a random template for the category
    template = random.choice(problem_templates[category])
    
    # Replace placeholders with random options
    for placeholder, options in variable_options.items():
        if "{" + placeholder + "}" in template:
            template = template.replace("{" + placeholder + "}", random.choice(options))
    
    return template.strip()

# Function to get sample problems
def get_sample_problems():
    """Return a dictionary of problem categories with freshly generated problems"""
    problems = {}
    for category in problem_templates.keys():
        problems[category] = generate_problem(category)
    return problems

# For static access, initialize a sample_problems dictionary
sample_problems = {category: generate_problem(category) for category in problem_templates.keys()}
