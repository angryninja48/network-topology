mock_cdp_result = {
    'csr01': [
        {'neighbor': 'csr02', 'local_interface': 'Gig 2', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 2'},
        {'neighbor': 'csr03', 'local_interface': 'Gig 3', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 3'}
    ],
    'csr02': [
        {'neighbor': 'csr01', 'local_interface': 'Gig 2', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 2'},
        {'neighbor': 'csr03', 'local_interface': 'Gig 4', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 4'}
    ],
    'csr03': [
        {'neighbor': 'csr01', 'local_interface': 'Gig 3', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 3'},
        {'neighbor': 'csr02', 'local_interface': 'Gig 4', 'capability': 'R I', 'platform': 'CSR1000V', 'neighbor_interface': 'Gig 4'}
    ]  
}
