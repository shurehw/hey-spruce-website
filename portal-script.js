// Supplier Portal JavaScript

// Sample contract templates
const contractTemplates = {
    standard: {
        name: "Standard Restaurant",
        serviceType: "nightly",
        frequency: "daily",
        services: ["kitchen", "floors", "equipment", "restrooms", "dining", "waste"],
        rate: 150,
        billing: "weekly",
        term: "1year",
        instructions: "Standard nightly cleaning service for full-service restaurants. Service performed after closing hours."
    },
    quickservice: {
        name: "Quick Service Restaurant",
        serviceType: "nightly",
        frequency: "daily",
        services: ["kitchen", "floors", "restrooms", "dining", "waste"],
        rate: 100,
        billing: "weekly",
        term: "6months",
        instructions: "Efficient cleaning service for fast-food and quick-service establishments."
    },
    bar: {
        name: "Bar & Nightclub",
        serviceType: "nightly",
        frequency: "daily",
        services: ["floors", "restrooms", "dining", "waste", "windows"],
        rate: 125,
        billing: "weekly",
        term: "1year",
        instructions: "Specialized after-hours cleaning for bars and entertainment venues. Focus on sticky floors and restroom sanitation."
    },
    kitchen: {
        name: "Ghost Kitchen",
        serviceType: "deep",
        frequency: "weekly",
        services: ["kitchen", "floors", "equipment", "hood", "grease"],
        rate: 200,
        billing: "monthly",
        term: "1year",
        instructions: "Kitchen-focused cleaning for delivery-only operations and ghost kitchens."
    },
    deepclean: {
        name: "Deep Clean Special",
        serviceType: "deep",
        frequency: "quarterly",
        services: ["kitchen", "floors", "equipment", "hood", "grease", "pressure"],
        rate: 800,
        billing: "perservice",
        term: "month",
        instructions: "Comprehensive deep cleaning service including all equipment, hood systems, and floor restoration."
    },
    emergency: {
        name: "Emergency Service",
        serviceType: "custom",
        frequency: "onetime",
        services: ["kitchen", "floors", "equipment", "restrooms", "emergency"],
        rate: 500,
        billing: "perservice",
        term: "month",
        instructions: "24/7 emergency response for failed health inspections. Immediate remediation and documentation provided."
    }
};

// Sample active contracts data
const sampleContracts = [
    {
        id: 1,
        client: "Joe's Pizza",
        serviceType: "Nightly Cleaning",
        frequency: "Daily",
        startDate: "2024-01-15",
        status: "active"
    },
    {
        id: 2,
        client: "The Blue Room Bar",
        serviceType: "Deep Clean",
        frequency: "Weekly",
        startDate: "2024-02-01",
        status: "active"
    },
    {
        id: 3,
        client: "Sakura Sushi",
        serviceType: "Kitchen & Hood",
        frequency: "Monthly",
        startDate: "2024-03-10",
        status: "pending"
    },
    {
        id: 4,
        client: "Burger Palace",
        serviceType: "Nightly Cleaning",
        frequency: "Daily",
        startDate: "2023-12-01",
        status: "expiring"
    }
];

// Toggle form sections
function openNewContract() {
    document.getElementById('contractForm').style.display = 'block';
    document.getElementById('templateSection').style.display = 'none';
    document.getElementById('activeContracts').style.display = 'none';
    document.getElementById('contractForm').scrollIntoView({ behavior: 'smooth' });
}

function openTemplates() {
    document.getElementById('contractForm').style.display = 'none';
    document.getElementById('templateSection').style.display = 'block';
    document.getElementById('activeContracts').style.display = 'none';
    document.getElementById('templateSection').scrollIntoView({ behavior: 'smooth' });
}

function viewActiveContracts() {
    document.getElementById('contractForm').style.display = 'none';
    document.getElementById('templateSection').style.display = 'none';
    document.getElementById('activeContracts').style.display = 'block';
    loadContracts();
    document.getElementById('activeContracts').scrollIntoView({ behavior: 'smooth' });
}

// Load template into form
function loadTemplate(templateName) {
    const template = contractTemplates[templateName];
    if (!template) return;
    
    // Fill form with template data
    document.querySelector('[name="serviceType"]').value = template.serviceType;
    document.querySelector('[name="frequency"]').value = template.frequency;
    document.querySelector('[name="rate"]').value = template.rate;
    document.querySelector('[name="billing"]').value = template.billing;
    document.querySelector('[name="contractTerm"]').value = template.term;
    document.querySelector('[name="instructions"]').value = template.instructions;
    
    // Clear all checkboxes first
    document.querySelectorAll('[name="services"]').forEach(cb => cb.checked = false);
    
    // Check services from template
    template.services.forEach(service => {
        const checkbox = document.querySelector(`[name="services"][value="${service}"]`);
        if (checkbox) checkbox.checked = true;
    });
    
    // Switch to form view
    openNewContract();
    
    // Show success message
    showNotification(`Template "${template.name}" loaded successfully!`);
}

// Update service options based on type
function updateServiceOptions() {
    const serviceType = document.querySelector('[name="serviceType"]').value;
    
    // Auto-select common services based on type
    const servicePresets = {
        nightly: ["kitchen", "floors", "restrooms", "dining", "waste"],
        deep: ["kitchen", "floors", "equipment", "hood", "grease"],
        hood: ["hood", "grease"],
        floor: ["floors", "pressure"],
        grease: ["grease", "waste"]
    };
    
    if (servicePresets[serviceType]) {
        document.querySelectorAll('[name="services"]').forEach(cb => cb.checked = false);
        servicePresets[serviceType].forEach(service => {
            const checkbox = document.querySelector(`[name="services"][value="${service}"]`);
            if (checkbox) checkbox.checked = true;
        });
    }
}

// Preview contract
function previewContract() {
    const form = document.getElementById('serviceContractForm');
    const formData = new FormData(form);
    
    // Generate contract document
    const contractHTML = generateContractHTML(formData);
    
    // Display in modal
    document.getElementById('contractDocument').innerHTML = contractHTML;
    document.getElementById('contractPreview').style.display = 'block';
}

// Generate contract HTML
function generateContractHTML(formData) {
    const businessName = formData.get('businessName') || '[Business Name]';
    const contactPerson = formData.get('contactPerson') || '[Contact Person]';
    const serviceAddress = formData.get('serviceAddress') || '[Service Address]';
    const startDate = formData.get('startDate') || '[Start Date]';
    const rate = formData.get('rate') || '[Rate]';
    const frequency = formData.get('frequency') || '[Frequency]';
    
    const services = formData.getAll('services');
    const servicesList = services.length > 0 ? 
        services.map(s => `<li>${s.charAt(0).toUpperCase() + s.slice(1).replace('_', ' ')}</li>`).join('') : 
        '<li>Services to be determined</li>';
    
    return `
        <div style="font-family: Georgia, serif; line-height: 1.8; color: #333;">
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1 style="color: #0a0a0a; font-size: 2rem;">GROUNDOPS</h1>
                <h2 style="color: #666; font-size: 1.5rem;">Commercial Cleaning Service Agreement</h2>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <p><strong>This Service Agreement</strong> ("Agreement") is entered into as of ${new Date().toLocaleDateString()} between:</p>
                
                <p style="margin: 1rem 0;">
                    <strong>Service Provider:</strong> GroundOps LLC<br>
                    1972 E 20th St, Los Angeles, CA 90058<br>
                    Phone: 877-253-2646<br>
                    Email: info@groundops.com
                </p>
                
                <p style="margin: 1rem 0;">
                    <strong>Client:</strong> ${businessName}<br>
                    Contact: ${contactPerson}<br>
                    Service Address: ${serviceAddress}<br>
                    Email: ${formData.get('email')}<br>
                    Phone: ${formData.get('phone')}
                </p>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #0a0a0a; border-bottom: 2px solid #0a0a0a; padding-bottom: 0.5rem;">1. SCOPE OF SERVICES</h3>
                <p>GroundOps agrees to provide the following cleaning services:</p>
                <ul style="margin: 1rem 0;">${servicesList}</ul>
                <p><strong>Frequency:</strong> ${frequency.charAt(0).toUpperCase() + frequency.slice(1)}</p>
                <p><strong>Start Date:</strong> ${startDate}</p>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #0a0a0a; border-bottom: 2px solid #0a0a0a; padding-bottom: 0.5rem;">2. PAYMENT TERMS</h3>
                <p><strong>Service Rate:</strong> $${rate} per service</p>
                <p><strong>Billing Cycle:</strong> ${formData.get('billing')}</p>
                <p><strong>Payment Terms:</strong> ${formData.get('paymentTerms')}</p>
                ${formData.get('discount') ? `<p><strong>Special Discount:</strong> ${formData.get('discount')}</p>` : ''}
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #0a0a0a; border-bottom: 2px solid #0a0a0a; padding-bottom: 0.5rem;">3. TERMS & CONDITIONS</h3>
                <ul style="margin: 1rem 0;">
                    <li>Service will be performed by trained and insured cleaning professionals</li>
                    <li>All cleaning supplies and equipment provided by GroundOps</li>
                    <li>Services comply with LA County Health Department regulations</li>
                    <li>24/7 emergency service available upon request</li>
                    <li>Client must provide access to service areas during scheduled times</li>
                    <li>Either party may terminate with 30 days written notice</li>
                </ul>
            </div>
            
            ${formData.get('insurance') ? `
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #0a0a0a; border-bottom: 2px solid #0a0a0a; padding-bottom: 0.5rem;">4. INSURANCE & LIABILITY</h3>
                <p>GroundOps maintains comprehensive general liability insurance of $2,000,000 and workers' compensation coverage for all employees. Certificates of insurance available upon request.</p>
            </div>
            ` : ''}
            
            ${formData.get('healthCompliance') ? `
            <div style="margin-bottom: 2rem;">
                <h3 style="color: #0a0a0a; border-bottom: 2px solid #0a0a0a; padding-bottom: 0.5rem;">5. HEALTH CODE COMPLIANCE GUARANTEE</h3>
                <p>GroundOps guarantees all services meet or exceed Los Angeles County Health Department standards. We provide documentation and support for all health inspections.</p>
            </div>
            ` : ''}
            
            <div style="margin-top: 3rem; border-top: 2px solid #5f6b9b; padding-top: 2rem;">
                <div style="display: flex; justify-content: space-between;">
                    <div style="width: 45%;">
                        <p><strong>CLIENT SIGNATURE</strong></p>
                        <div style="border-bottom: 1px solid #333; margin: 2rem 0;"></div>
                        <p>${contactPerson}<br>${businessName}<br>Date: _____________</p>
                    </div>
                    <div style="width: 45%;">
                        <p><strong>GROUNDOPS REPRESENTATIVE</strong></p>
                        <div style="border-bottom: 1px solid #333; margin: 2rem 0;"></div>
                        <p>Authorized Signature<br>GroundOps LLC<br>Date: _____________</p>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Send contract
function sendContract() {
    const form = document.getElementById('serviceContractForm');
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }
    
    // In production, this would send the contract via email
    showNotification('Contract sent successfully! Client will receive email with DocuSign link.');
    
    // Add to active contracts
    const formData = new FormData(form);
    const newContract = {
        id: Date.now(),
        client: formData.get('businessName'),
        serviceType: formData.get('serviceType'),
        frequency: formData.get('frequency'),
        startDate: formData.get('startDate'),
        status: 'pending'
    };
    
    // Reset form
    form.reset();
}

// Save as template
function saveTemplate() {
    const templateName = prompt('Enter template name:');
    if (!templateName) return;
    
    // In production, this would save to database
    showNotification(`Template "${templateName}" saved successfully!`);
}

// Load contracts table
function loadContracts() {
    const tbody = document.getElementById('contractsTableBody');
    tbody.innerHTML = '';
    
    sampleContracts.forEach(contract => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${contract.client}</td>
            <td>${contract.serviceType}</td>
            <td>${contract.frequency}</td>
            <td>${contract.startDate}</td>
            <td><span class="status-badge status-${contract.status}">${contract.status.toUpperCase()}</span></td>
            <td>
                <div class="action-buttons">
                    <button class="action-btn" onclick="viewContract(${contract.id})" title="View">👁️</button>
                    <button class="action-btn" onclick="editContract(${contract.id})" title="Edit">✏️</button>
                    <button class="action-btn" onclick="renewContract(${contract.id})" title="Renew">🔄</button>
                </div>
            </td>
        `;
        tbody.appendChild(row);
    });
}

// Contract actions
function viewContract(id) {
    showNotification(`Viewing contract #${id}`);
}

function editContract(id) {
    showNotification(`Editing contract #${id}`);
}

function renewContract(id) {
    showNotification(`Renewing contract #${id}`);
}

// Close preview modal
function closePreview() {
    document.getElementById('contractPreview').style.display = 'none';
}

// Download PDF (placeholder)
function downloadPDF() {
    showNotification('Generating PDF... In production, this would use a PDF library.');
    window.print();
}

// Email contract (placeholder)
function emailContract() {
    const email = prompt('Enter recipient email:');
    if (email) {
        showNotification(`Contract sent to ${email}`);
    }
}

// Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #0a0a0a;
        color: #ffffff;
        padding: 0.75rem 1.25rem;
        font-family: 'Inter', sans-serif;
        font-size: 0.8125rem;
        z-index: 10000;
        opacity: 0;
        transition: opacity 150ms ease;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);
    requestAnimationFrame(() => { notification.style.opacity = '1'; });

    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 150);
    }, 3000);
}

// Logout function
function logout() {
    if (confirm('Are you sure you want to logout?')) {
        window.location.href = '/';
    }
}

// Search contracts
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('contractSearch');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('#contractsTableBody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    }
    
    // Filter by status
    const filterSelect = document.getElementById('filterStatus');
    if (filterSelect) {
        filterSelect.addEventListener('change', function(e) {
            const status = e.target.value;
            const rows = document.querySelectorAll('#contractsTableBody tr');
            
            rows.forEach(row => {
                if (status === 'all') {
                    row.style.display = '';
                } else {
                    const badge = row.querySelector('.status-badge');
                    const rowStatus = badge ? badge.textContent.toLowerCase() : '';
                    row.style.display = rowStatus === status ? '' : 'none';
                }
            });
        });
    }
});

